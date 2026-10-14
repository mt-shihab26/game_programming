#pragma once

#include "opengl/renderer.hpp"

class OpenGLLayer {
  public:
    OpenGLLayer();

    void begin_frame() const;

  private:
    Renderer m_renderer;
};
