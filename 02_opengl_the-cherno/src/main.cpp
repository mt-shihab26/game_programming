#include <cstdlib>

#include <glew/GL/glew.h>
#include <glfw/GLFW/glfw3.h>
#include "glm/ext/matrix_clip_space.hpp"
#include "glm/ext/matrix_transform.hpp"
#include "glm/ext/vector_float3.hpp"
#include <imgui/imgui.h>
#include <imgui/imgui_impl_glfw.h>
#include <imgui/imgui_impl_opengl3.h>

#include "supports/helper.hpp"
#include "supports/window.hpp"

#include "shader.hpp"
#include "texture.hpp"
#include "renderer.hpp"
#include "vertex_buffer.hpp"
#include "index_buffer.hpp"
#include "vertex_array.hpp"
#include "vertex_buffer_layout.hpp"

int main() {
    const int width = 1280;
    const int height = 780;

    GLFWwindow *window;

    // Mesa returns the newest version it has, so pin it to 3.3
    setenv("MESA_GL_VERSION_OVERRIDE", "3.3", 1);
    setenv("MESA_GLSL_VERSION_OVERRIDE", "330", 1);

    if (!glfwInit()) {
        return 1;
    }

    glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    window = glfwCreateWindow(width, height, "Hello World", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return 1;
    }

    glfwMakeContextCurrent(window);

    wait_for_window_size(window, width, height);

    glfwSwapInterval(1);

    if (glewInit() != GLEW_OK) {
        glfwTerminate();
        return 1;
    }

    print_libaray_versions();

    {
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
        glm::mat4 view = glm::translate(glm::mat4(1.0f), glm::vec3(-100, 0, 0));

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

        ImGui::CreateContext();
        ImGui_ImplGlfw_InitForOpenGL(window, true);
        ImGui_ImplOpenGL3_Init("#version 330");
        ImGui::StyleColorsDark();
        ImGuiIO &io = ImGui::GetIO();
        // window positions and sizes are set in code, so don't save them to imgui.ini
        io.IniFilename = nullptr;
        // the default pixel font looks jagged at fractional scales (1.25), the vector one stays crisp
        io.Fonts->AddFontDefaultVector();
        // scale text and widgets by the monitor scale, otherwise the 13px font is only ~16 real pixels tall
        // GLFW's content scale reports 1.0 on Wayland fractional scaling, so derive it from the framebuffer
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

        glm::vec3 translation(200, 200, 0);

        while (!glfwWindowShouldClose(window)) {
            renderer.clear();

            ImGui_ImplOpenGL3_NewFrame();
            ImGui_ImplGlfw_NewFrame();
            ImGui::NewFrame();

            glm::mat4 model = glm::translate(glm::mat4(1.0), translation);
            glm::mat4 mvp = proj * view * model;

            shader.bind();
            shader.set_uniform_mat4f("u_mvp", mvp);

            renderer.draw(va, ib, shader);

            {
                ImGui::SetNextWindowPos(ImVec2(60 * content_scale, 60 * content_scale), ImGuiCond_FirstUseEver);
                ImGui::SetNextWindowSize(ImVec2(340 * content_scale, 180 * content_scale), ImGuiCond_FirstUseEver);
                ImGui::Begin("Controls");

                ImGui::SliderFloat3("Translation", &translation.x, 0.0f, (float)width);
                ImGui::Text("Application average %.3f ms/frame (%.1f FPS)", 1000.0f / io.Framerate, io.Framerate);

                ImGui::End();
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
