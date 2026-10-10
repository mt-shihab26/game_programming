#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include "helper.hpp"
#include "index_buffer.hpp"

IndexBuffer::IndexBuffer(const unsigned int *data, unsigned int count) : m_count(count) {
    ASSERT(sizeof(unsigned int) == sizeof(GLuint));

    GL_CALL(glGenBuffers(1, &m_renderer_id));
    GL_CALL(glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_renderer_id));
    GL_CALL(glBufferData(GL_ELEMENT_ARRAY_BUFFER, count * sizeof(unsigned int), data, GL_STATIC_DRAW));
}

IndexBuffer::~IndexBuffer() {}

void IndexBuffer::bind() const {
    GL_CALL(glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_renderer_id));
}

void IndexBuffer::unbind() const {
    GL_CALL(glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0));
}
