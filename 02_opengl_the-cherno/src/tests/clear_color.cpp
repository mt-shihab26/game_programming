#include <glew/GL/glew.h>
#include <imgui/imgui.h>

#include "opengl/helper.hpp"

#include "clear_color.hpp"

namespace test {

ClearColor::ClearColor() : m_clear_color{0.2f, 0.3f, 0.8f, 1.0f} {
}

ClearColor::~ClearColor() {
}

void ClearColor::on_update(float dt) {
}

void ClearColor::on_render() {
    GL_CALL(glClearColor(m_clear_color[0], m_clear_color[1], m_clear_color[2], m_clear_color[3]));
    GL_CALL(glClear(GL_COLOR_BUFFER_BIT));
}

void ClearColor::on_imgui_render() {
    ImGui::ColorEdit4("Clear Color", m_clear_color);
}

} // namespace test
