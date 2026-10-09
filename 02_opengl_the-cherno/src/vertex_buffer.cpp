#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include "renderer.hpp"
#include "vertex_buffer.hpp"

VertexBuffer::VertexBuffer(const void *data, unsigned int size) {
    GL_CALL(glGenBuffers(1, &m_renderer_id));
    GL_CALL(glBindBuffer(GL_ARRAY_BUFFER, m_renderer_id));
    GL_CALL(glBufferData(GL_ARRAY_BUFFER, size, data, GL_STATIC_DRAW));
}

VertexBuffer::~VertexBuffer() {
    GL_CALL(glDeleteBuffers(1, &m_renderer_id));
}

void VertexBuffer::bind() const {
    GL_CALL(glBindBuffer(GL_ARRAY_BUFFER, m_renderer_id));
}

void VertexBuffer::unbind() const {
    GL_CALL(glBindBuffer(GL_ARRAY_BUFFER, 0));
}
