#include <glew/GL/glew.h>
#include <imgui/imgui.h>
#include "core/log.hpp"
#include "opengl/helper.hpp"
#include "test_clear_color.hpp"

TestClearColor::TestClearColor(const std::string &key, const std::string &name) : Test(key, name), m_clear_color{0.2f, 0.3f, 0.8f, 1.0f} {
    log_info("Opened test '{}' (key: {})", get_name(), get_key());
}

TestClearColor::~TestClearColor() {
    log_info("Closed test '{}' (key: {})", get_name(), get_key());
}

void TestClearColor::on_render() {
    GL_CALL(glClearColor(m_clear_color[0], m_clear_color[1], m_clear_color[2], m_clear_color[3]));
    GL_CALL(glClear(GL_COLOR_BUFFER_BIT));
}

void TestClearColor::on_imgui_render() {
    ImGui::ColorEdit4("Clear Color", m_clear_color);
}
