#include <glew/GL/glew.h>
#include <glm/ext/matrix_clip_space.hpp>
#include <glm/ext/matrix_transform.hpp>
#include <glm/ext/vector_float3.hpp>
#include <glm/glm.hpp>
#include <imgui/imgui.h>
#include <imgui/imgui_impl_glfw.h>
#include <imgui/imgui_impl_opengl3.h>

#include "orthographic_camera.hpp"

glm::mat4 OrthographicCamera::get_view_projection() const {
    return get_projection() * get_view();
}

glm::mat4 OrthographicCamera::get_projection() const {
    ImGuiIO &io = ImGui::GetIO();
    return glm::ortho(0.0f, io.DisplaySize.x, 0.0f, io.DisplaySize.y, -1.0f, 1.0f);
}

glm::mat4 OrthographicCamera::get_view() const {
    return glm::translate(glm::mat4(1.0f), glm::vec3(0, 0, 0));
}
