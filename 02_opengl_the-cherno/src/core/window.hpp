#pragma once

#include <string>

struct GLFWwindow;

// Owns GLFW and the OpenGL 4.6 core context. Throws std::runtime_error if either fails to start.
class Window {
  public:
    Window(int width, int height, const std::string &title);
    ~Window();

    bool should_close() const;
    // shows the finished frame and handles input and window events
    void end_frame() const;

    // ratio of framebuffer pixels to window units, e.g. 1.25 on a display scaled to 125%
    float content_scale() const;

    GLFWwindow *handle() const { return m_window; }

  private:
    GLFWwindow *m_window;
};
