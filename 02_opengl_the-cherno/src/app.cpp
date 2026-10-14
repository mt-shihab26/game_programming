#include "tests/test_clear_color.hpp"

#include "app.hpp"

App::App() : m_window(1280, 780, "OpenGL - The Cherno"), m_imgui_layer(m_window) {
    m_test_menu.register_test<TestClearColor>("Clear Color");
}

void App::run() {
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
