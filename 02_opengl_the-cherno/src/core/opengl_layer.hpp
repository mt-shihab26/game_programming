#pragma once

#include "opengl/renderer.hpp"

// Loads the OpenGL functions (GLEW), sets the global GL state and clears the screen each frame.
// Needs a current context, so create it after the Window. Throws std::runtime_error if GLEW fails to load.
class OpenGLLayer {
  public:
    OpenGLLayer();

    OpenGLLayer(const OpenGLLayer &) = delete;
    OpenGLLayer &operator=(const OpenGLLayer &) = delete;

    void begin_frame() const;

    const Renderer &renderer() const { return m_renderer; }

  private:
    Renderer m_renderer;
};
