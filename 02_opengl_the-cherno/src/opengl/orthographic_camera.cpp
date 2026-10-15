#include <glew/GL/glew.h>
#include <glm/ext/matrix_clip_space.hpp>
#include <glm/ext/matrix_transform.hpp>
#include <glm/ext/vector_float3.hpp>
#include <glm/glm.hpp>
#include <imgui/imgui.h>
#include <imgui/imgui_impl_glfw.h>
#include <imgui/imgui_impl_opengl3.h>

#include "orthographic_camera.hpp"

OrthographicCamera::OrthographicCamera() : m_zoom(1.0f) {
    m_view = glm::translate(glm::mat4(1.0f), glm::vec3(0, 0, 0));

    set_viewport();
    set_projection();
}

void OrthographicCamera::on_update() {
    set_viewport();
    handle_mouse_wheel_update();
    set_projection();
}

void OrthographicCamera::handle_mouse_wheel_update() {
    float wheel = ImGui::GetIO().MouseWheel;
    if (wheel) {
        m_zoom = m_zoom + wheel * 0.1f;
    }
}

void OrthographicCamera::set_viewport() {
    ImGuiIO &io = ImGui::GetIO();
    m_width = io.DisplaySize.x;
    m_height = io.DisplaySize.y;
}

void OrthographicCamera::set_projection() {
    float zoom = (m_zoom == 0.0f ? 1 : m_zoom);
    float half_width = m_width / 2.0f / zoom;
    float half_height = m_height / 2.0f / zoom;
    m_projection = glm::ortho(-half_width, half_width, -half_height, half_height, -1.0f, 1.0f);
}

void OrthographicCamera::on_render() {
}

void OrthographicCamera::on_imgui_render() {
    ImVec2 top_right(ImGui::GetIO().DisplaySize.x - 10.0f, 10.0f);
    ImGui::SetNextWindowPos(top_right, ImGuiCond_Always, ImVec2(1.0f, 0.0f));

    ImGui::Begin("Camera", nullptr, ImGuiWindowFlags_NoDecoration | ImGuiWindowFlags_NoMove | ImGuiWindowFlags_AlwaysAutoResize);

    ImGui::Text("zoom = %.2f", m_zoom);

    ImGui::End();
}
