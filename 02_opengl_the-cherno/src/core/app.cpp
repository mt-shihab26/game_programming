#include <glew/GL/glew.h>

#include "supports/helper.hpp"
#include "tests/clear_color.hpp"

#include "app.hpp"

App::App() : m_window(1280, 780, "Hello World"), m_imgui(m_window) {
    GL_CALL(glEnable(GL_BLEND));
    GL_CALL(glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA));

    m_tests.register_test<test::ClearColor>("Clear Color");
}

void App::run() {
    while (!m_window.should_close()) {
        m_renderer.clear();

        m_imgui.begin_frame();

        m_tests.on_update(0.0f);
        m_tests.on_render();
        m_tests.on_imgui_render();

        m_imgui.end_frame();

        m_window.swap_buffers();
        m_window.poll_events();
    }
}
