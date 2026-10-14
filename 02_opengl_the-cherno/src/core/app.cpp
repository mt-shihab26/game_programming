#include <glew/GL/glew.h>

#include "opengl/helper.hpp"
#include "tests/clear_color.hpp"

#include "app.hpp"

App::App() : m_window(1280, 780, "Hello World"), m_imgui_layer(m_window) {
    GL_CALL(glEnable(GL_BLEND));
    GL_CALL(glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA));

    m_test_runner.register_test<test::ClearColor>("Clear Color");
}

void App::run() {
    while (!m_window.should_close()) {
        m_renderer.clear();

        m_imgui_layer.begin_frame();

        m_test_runner.on_update(0.0f);
        m_test_runner.on_render();
        m_test_runner.on_imgui_render();

        m_imgui_layer.end_frame();

        m_window.swap_buffers();
        m_window.poll_events();
    }
}
