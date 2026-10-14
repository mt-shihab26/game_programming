#pragma once

#include <string>

struct GLFWwindow;

// Owns GLFW, the OpenGL 3.3 core context and GLEW. Throws std::runtime_error if any of them fail to start.
class Window {
  public:
    Window(int width, int height, const std::string &title);
    ~Window();

    Window(const Window &) = delete;
    Window &operator=(const Window &) = delete;

    bool should_close() const;
    void swap_buffers() const;
    void poll_events() const;

    // ratio of framebuffer pixels to window units, e.g. 1.25 on a display scaled to 125%
    float content_scale() const;

    GLFWwindow *handle() const { return m_window; }

  private:
    GLFWwindow *m_window;
};
