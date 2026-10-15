#include <glew/GL/glew.h>
#include <glm/ext/matrix_clip_space.hpp>
#include <glm/ext/matrix_transform.hpp>
#include <glm/ext/vector_float3.hpp>
#include <glm/glm.hpp>
#include <imgui/imgui.h>
#include <imgui/imgui_impl_glfw.h>
#include <imgui/imgui_impl_opengl3.h>

#include "orthographic_camera.hpp"

OrthographicCamera::OrthographicCamera() {
    set_default();
}

void OrthographicCamera::on_update() {
    set_viewport();

    ImGuiIO &io = ImGui::GetIO();

    if (!io.WantCaptureMouse) {
        handle_mouse_wheel_update();
        handle_mouse_drag_update();
    }

    if (!io.WantCaptureKeyboard) {
        handle_reset_shortcut();
    }
}

void OrthographicCamera::handle_mouse_drag_update() {
    if (ImGui::IsMouseDragging(ImGuiMouseButton_Left)) {
        ImVec2 delta = ImGui::GetMouseDragDelta(ImGuiMouseButton_Left);
        ImGui::ResetMouseDragDelta(ImGuiMouseButton_Left);
        set_view(m_position + glm::vec3(delta.x, -delta.y, 0) / m_zoom);
    }
}

void OrthographicCamera::handle_reset_shortcut() {
    if (ImGui::IsKeyChordPressed(ImGuiMod_Ctrl | ImGuiKey_R)) {
        set_default();
    }
}

void OrthographicCamera::handle_mouse_wheel_update() {
    float wheel = ImGui::GetIO().MouseWheel;
    if (wheel > 0) {
        set_projection(m_width, m_height, m_zoom * 1.1f);
    }
    if (wheel < 0) {
        set_projection(m_width, m_height, m_zoom / 1.1f);
    }
}

void OrthographicCamera::on_render() {
}

void OrthographicCamera::on_imgui_render() {
    ImGui::SetNextWindowPos(ImVec2(10.0f, 10.0f), ImGuiCond_Always);

    ImGui::Begin("Camera", nullptr, ImGuiWindowFlags_NoDecoration | ImGuiWindowFlags_NoMove | ImGuiWindowFlags_AlwaysAutoResize);

    ImGui::Text("zoom = %.2e", m_zoom);
    ImGui::Text("position = %.2f, %.2f", m_position.x, m_position.y);
    ImGui::Text("viewport = %.0f x %.0f", m_width, m_height);

    ImGui::End();
}

void OrthographicCamera::set_default() {
    set_view(glm::vec3(0, 0, 0));
    set_projection(m_width, m_height, 1.0f);
}

void OrthographicCamera::set_viewport() {
    ImGuiIO &io = ImGui::GetIO();
    if (io.DisplaySize.x != m_width || io.DisplaySize.y != m_height) {
        set_projection(io.DisplaySize.x, io.DisplaySize.y, m_zoom);
    }
}

void OrthographicCamera::set_view(const glm::vec3 &position) {
    m_position = position;
    m_view = glm::translate(glm::mat4(1.0f), m_position);
}

void OrthographicCamera::set_projection(float width, float height, float zoom) {
    m_width = width;
    m_height = height;
    m_zoom = zoom;

    float half_width = m_width / 2.0f / m_zoom;
    float half_height = m_height / 2.0f / m_zoom;
    m_projection = glm::ortho(-half_width, half_width, -half_height, half_height, -1.0f, 1.0f);
}
