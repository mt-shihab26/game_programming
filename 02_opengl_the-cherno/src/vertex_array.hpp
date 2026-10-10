#pragma once

#include "vertex_buffer.hpp"
#include "vertex_buffer_layout.hpp"

class VertexArray {
  private:
  public:
    VertexArray();
    ~VertexArray();

    void add_buffer(const VertexBuffer &vb, const VertexBufferLayout &layout);
};
