#include <GL/glew.h>

#include "renderer.hpp"
#include "vertex_buffer.hpp"
#include "vertex_array.hpp"

VertexArray::VertexArray() {
}
VertexArray::~VertexArray() {}

void VertexArray::add_buffer(const VertexBuffer &vb, const VertexBufferLayout &layout) {
    vb.bind();

    const auto &elements = layout.get_elements();

    GL_CALL(glEnableVertexAttribArray(0));
    GL_CALL(glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, sizeof(float) * 2, 0));
}
