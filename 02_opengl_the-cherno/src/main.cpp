#include <exception>
#include <iostream>

#include "core/imgui_layer.hpp"
#include "core/opengl_layer.hpp"
#include "core/test_menu.hpp"
#include "core/window.hpp"

#include "tests/test_clear_color.hpp"

class App {
  public:
    App() : m_window(1280, 780, "OpenGL - The Cherno"), m_imgui_layer(m_window) {
        m_test_menu.register_test<TestClearColor>("Clear Color");
    }

    void run() {
        while (!m_window.should_close()) {
            m_opengl_layer.begin_frame();
            m_imgui_layer.begin_frame();

            m_test_menu.on_update(0.0f);
            m_test_menu.on_render();
            m_test_menu.on_imgui_render();

            m_imgui_layer.end_frame();

            m_window.end_frame();
        }
    }

  private:
    Window m_window;
    OpenGLLayer m_opengl_layer;
    ImGuiLayer m_imgui_layer;
    TestMenu m_test_menu;
};

int main() {
    try {
        App app;
        app.run();
    } catch (const std::exception &error) {
        std::cerr << "error: " << error.what() << std::endl;
        return 1;
    }
    return 0;
}
