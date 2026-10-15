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
    glm::mat4 get_view_projection() const;

  private:
    glm::mat4 get_projection() const;
    glm::mat4 get_view() const;
};
