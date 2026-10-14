#pragma once

#include "opengl/renderer.hpp"

class OpenGLLayer {
  public:
    OpenGLLayer();

    void begin_frame() const;

    const Renderer &renderer() const { return m_renderer; }

  private:
    Renderer m_renderer;
};
