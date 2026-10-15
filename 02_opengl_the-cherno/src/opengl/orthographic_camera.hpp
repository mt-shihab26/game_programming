#pragma once

#include <glew/GL/glew.h>
#include <glm/ext/matrix_clip_space.hpp>
#include <glm/ext/matrix_transform.hpp>
#include <glm/ext/vector_float3.hpp>
#include <glm/glm.hpp>
#include <imgui/imgui.h>
#include <imgui/imgui_impl_glfw.h>
#include <imgui/imgui_impl_opengl3.h>

class OrthographicCamera {
  public:
    glm::mat4 get_view_projection() const {
        return get_projection() * get_view();
    }

  private:
    glm::mat4 get_projection() const {
        ImGuiIO &io = ImGui::GetIO();
        return glm::ortho(0.0f, io.DisplaySize.x, 0.0f, io.DisplaySize.y, -1.0f, 1.0f);
    }

    glm::mat4 get_view() const {
        return glm::translate(glm::mat4(1.0f), glm::vec3(0, 0, 0));
    }
};
