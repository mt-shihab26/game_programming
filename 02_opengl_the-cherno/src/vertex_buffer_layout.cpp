#include <GL/glew.h>

#include "vertex_buffer_layout.hpp"

template <>
void VertexBufferLayout::push<float>(unsigned int count) {
    m_elements.push_back({GL_FLOAT, count, false});
}

template <>
void VertexBufferLayout::push<unsigned int>(unsigned int count) {
    m_elements.push_back({GL_UNSIGNED_INT, count, false});
}

template <>
void VertexBufferLayout::push<unsigned char>(unsigned int count) {
    m_elements.push_back({GL_UNSIGNED_BYTE, count, true});
}
