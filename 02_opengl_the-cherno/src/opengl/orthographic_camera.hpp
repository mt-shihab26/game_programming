#pragma once

#include <glm/glm.hpp>

class OrthographicCamera {
  public:
    OrthographicCamera();

    void on_update();
    void on_render();
    bool on_imgui_render();

    glm::mat4 get_view_projection() const { return get_projection() * get_view(); }

  private:
    float m_width = 0.0f;
    float m_height = 0.0f;
    glm::mat4 m_projection;
    glm::mat4 m_view;

    float m_zoom;
    glm::vec3 m_position;

    void set_default();
    void set_viewport();
    void handle_mouse_wheel_update();
    void handle_reset_shortcut();
    void handle_mouse_drag_update();
    void set_view(const glm::vec3 &position);
    void set_projection(float width, float height, float zoom);

    glm::mat4 get_projection() const { return m_projection; }
    glm::mat4 get_view() const { return m_view; }
};
