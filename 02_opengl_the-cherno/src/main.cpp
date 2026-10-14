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
#include "tests/test.hpp"
#include "texture.hpp"
#include "renderer.hpp"
#include "tests/clear_color.hpp"
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
        GL_CALL(glEnable(GL_BLEND));
        GL_CALL(glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA));

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

        test::Test *current_test = nullptr;
        test::Menu *menu = new test::Menu(current_test);
        current_test = menu;

        while (!glfwWindowShouldClose(window)) {

            renderer.clear();

            ImGui_ImplOpenGL3_NewFrame();
            ImGui_ImplGlfw_NewFrame();
            ImGui::NewFrame();

            if (current_test) {
                current_test->on_update(0.0f);
                current_test->on_render();

                ImGui::Begin("Test");
                if (current_test != menu) {
                    if (ImGui::Button("<-")) {
                        delete current_test;
                        current_test = menu;
                    }
                }
                current_test->on_imgui_render();
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
