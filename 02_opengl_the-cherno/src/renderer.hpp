#pragma once

#include "index_buffer.hpp"
#include "shader.hpp"
#include "vertex_array.hpp"

class Renderer {
  private:
  public:
    void draw(const VertexArray &va, const IndexBuffer &ib, const Shader &shader) const;
};
