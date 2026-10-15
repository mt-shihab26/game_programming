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
    OrthographicCamera();

    void on_update();
    void on_render();
    void on_imgui_render();

    glm::mat4 get_view_projection() const { return get_projection() * get_view(); }

  private:
    float m_width;
    float m_height;
    glm::mat4 m_projection;
    glm::mat4 m_view;

    float m_zoom;

    void set_viewport();
    void handle_mouse_wheel_update();
    void set_projection();

    glm::mat4 get_projection() const { return m_projection; }
    glm::mat4 get_view() const { return m_view; }
};
