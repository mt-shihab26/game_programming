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
    set_viewport();
}

OrthographicCamera::~OrthographicCamera() {
}

void OrthographicCamera::set_viewport() {
    ImGuiIO &io = ImGui::GetIO();
    m_width = io.DisplaySize.x;
    m_height = io.DisplaySize.y;
}

glm::mat4 OrthographicCamera::get_view_projection() const {
    return get_projection() * get_view();
}

glm::mat4 OrthographicCamera::get_projection() const {
    return glm::ortho(0.0f, m_width, 0.0f, m_height, -1.0f, 1.0f);
}

glm::mat4 OrthographicCamera::get_view() const {
    return glm::translate(glm::mat4(1.0f), glm::vec3(0, 0, 0));
}
