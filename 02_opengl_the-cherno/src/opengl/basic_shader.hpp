#pragma once

#include <string>

#include <glew/GL/glew.h>

class BasicShader {
  public:
    BasicShader(const std::string &filepath);
    ~BasicShader();

    GLuint get_renderer_id() const { return m_renderer_id; }

  private:
    GLuint m_renderer_id;
};
