#include "test_clear_color.hpp"
#include "core/log.hpp"
#include "opengl/helper.hpp"
#include "opengl/orthographic_camera.hpp"
#include <glew/GL/glew.h>
#include <imgui/imgui.h>

TestClearColor::TestClearColor(const std::string &key, const std::string &name, OrthographicCamera *camera)
    : Test(key, name, camera), m_clear_color{0.2f, 0.3f, 0.8f, 1.0f} {
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
    // SetNextWindow* only applies to the next Begin(), so it has to be set here, before the test's window opens
    float content_scale = ImGui::GetIO().DisplayFramebufferScale.x;
    // pivot (1, 0) anchors the window by its top-right corner
    ImVec2 top_right(ImGui::GetIO().DisplaySize.x, 0.0f);
    ImGui::SetNextWindowPos(top_right, ImGuiCond_Appearing, ImVec2(1.0f, 0.0f));
    ImGui::SetNextWindowSize(ImVec2(340 * content_scale, 180 * content_scale), ImGuiCond_FirstUseEver);

    ImGui::Begin(get_name().c_str());
    ImGui::ColorEdit4("Clear Color", m_clear_color);
    ImGui::End();
}
