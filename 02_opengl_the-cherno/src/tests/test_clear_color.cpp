#include <glew/GL/glew.h>

#include "supports/helper.hpp"

#include "test_clear_color.hpp"

namespace test {

TestClearColor::TestClearColor() : m_clear_color{0.2f, 0.3f, 0.8f, 1.0f} {
}

TestClearColor::~TestClearColor() {}

void TestClearColor::on_update(float dt) {}

void TestClearColor::on_render() {
    GL_CALL(glClearColor(m_clear_color[0], m_clear_color[2], m_clear_color[2], m_clear_color[3]));
}

void TestClearColor::on_imgui_render() {}

} // namespace test
