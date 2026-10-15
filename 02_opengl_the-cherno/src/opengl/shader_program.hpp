#pragma once

#include <string>

#include <glew/GL/glew.h>

class ShaderProgram {
  public:
    ShaderProgram(const std::string &filepath);
    ~ShaderProgram();

    GLuint get_renderer_id() const { return m_renderer_id; }

  private:
    GLuint m_renderer_id;
};
