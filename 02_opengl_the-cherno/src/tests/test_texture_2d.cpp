#include <glew/GL/glew.h>
#include <glm/glm.hpp>
#include "glm/ext/matrix_clip_space.hpp"
#include "glm/ext/matrix_transform.hpp"
#include "glm/ext/vector_float3.hpp"
#include <imgui/imgui.h>
#include <imgui/imgui_impl_glfw.h>
#include <imgui/imgui_impl_opengl3.h>

#include "core/log.hpp"
#include "opengl/helper.hpp"
#include "opengl/vertex_array.hpp"
#include "opengl/vertex_buffer.hpp"
#include "opengl/index_buffer.hpp"
#include "opengl/shader.hpp"
#include "opengl/texture.hpp"
#include "opengl/renderer.hpp"

#include "test_texture_2d.hpp"

TestTexture2D::TestTexture2D(const std::string &key, const std::string &name) : Test(key, name) {
    log_info("Opened test '{}' (key: {})", get_name(), get_key());

    const int width = 1280;
    const int height = 780;

    // clang-format off
    float positions[] = {
        -50.0f, -50.0f, 0.0f, 0.0f, // 0
         50.0f, -50.0f, 1.0f, 0.0f, // 1
         50.0f,  50.5f, 1.0f, 1.0f, // 2
        -50.0f,  50.5f, 0.0f, 1.0f  // 3
    };

    unsigned int indices[] = {
        0, 1, 2,
        2, 3, 0
    };
    // clang-format on

    GL_CALL(glEnable(GL_BLEND));
    GL_CALL(glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA));

    VertexArray va;

    VertexBuffer vb(positions, 4 * 4 * sizeof(float));

    VertexBufferLayout layout;
    layout.push<float>(2);
    layout.push<float>(2);
    va.add_buffer(vb, layout);

    IndexBuffer ib(indices, 6);

    glm::mat4 proj = glm::ortho(0.0f, (float)width, 0.0f, (float)height, -1.0f, 1.0f);
    glm::mat4 view = glm::translate(glm::mat4(1.0f), glm::vec3(0, 0, 0));

    Shader shader("assets/shaders/basic.glsl");
    shader.bind();
    shader.set_uniform_1i("u_texture", 0);

    Texture texture("assets/textures/omarchy-logo-tokyo-night.png");
    texture.bind();

    va.unbind();
    shader.unbind();
    vb.unbind();
    ib.unbind();

    Renderer renderer;

    glm::vec3 translation_a(200, 200, 0);
    glm::vec3 translation_b(400, 200, 0);

    while (!glfwWindowShouldClose(window)) {
        renderer.clear();
        {
            glm::mat4 model = glm::translate(glm::mat4(1.0), translation_a);
            glm::mat4 mvp = proj * view * model;

            shader.bind();
            shader.set_uniform_mat4f("u_mvp", mvp);

            renderer.draw(va, ib, shader);
        }

        {
            glm::mat4 model = glm::translate(glm::mat4(1.0), translation_b);
            glm::mat4 mvp = proj * view * model;

            shader.bind();
            shader.set_uniform_mat4f("u_mvp", mvp);

            renderer.draw(va, ib, shader);
        }

        ImGui::Render();
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    ImGui_ImplOpenGL3_Shutdown();
    ImGui_ImplGlfw_Shutdown();
    ImGui::DestroyContext();
}

glfwTerminate();

return 0;
}

TestTexture2D::~TestTexture2D() {
    log_info("Closed test '{}' (key: {})", get_name(), get_key());
}

void TestTexture2D::on_update(float dt) {
}

void TestTexture2D::on_render() {
}

void TestTexture2D::on_imgui_render() {
    int framebuffer_width, window_width;
    glfwGetFramebufferSize(window, &framebuffer_width, nullptr);
    glfwGetWindowSize(window, &window_width, nullptr);
    float content_scale = (float)framebuffer_width / (float)window_width;
    ImGuiStyle &style = ImGui::GetStyle();
    style.ScaleAllSizes(content_scale);
    style.FontScaleDpi = content_scale;

    bool show_demo_window = true;
    bool show_another_window = false;
    ImVec4 clear_color = ImVec4(0.45f, 0.55f, 0.60f, 1.00f);

    {
        ImGui::SetNextWindowPos(ImVec2(60 * content_scale, 60 * content_scale), ImGuiCond_FirstUseEver);
        ImGui::SetNextWindowSize(ImVec2(340 * content_scale, 180 * content_scale), ImGuiCond_FirstUseEver);
        ImGui::Begin("Controls");

        ImGui::SliderFloat3("Translation A", &translation_a.x, 0.0f, (float)width);
        ImGui::SliderFloat3("Translation B", &translation_b.x, 0.0f, (float)width);
        ImGui::Text("Application average %.3f ms/frame (%.1f FPS)", 1000.0f / io.Framerate, io.Framerate);

        ImGui::End();
    }
}
