#include <GL/glew.h>

#include "helper.hpp"
#include "vertex_buffer.hpp"
#include "vertex_buffer_layout.hpp"
#include "vertex_array.hpp"

VertexArray::VertexArray() {
    GL_CALL(glGenVertexArrays(1, &m_renderer_id));
}
VertexArray::~VertexArray() {
    GL_CALL(glDeleteVertexArrays(1, &m_renderer_id));
}

void VertexArray::add_buffer(const VertexBuffer &vb, const VertexBufferLayout &layout) {
    bind();
    vb.bind();

    const auto &elements = layout.get_elements();
    unsigned long int offset = 0;
    for (unsigned int i = 0; i < elements.size(); i++) {
        const auto &element = elements[i];
        GL_CALL(glEnableVertexAttribArray(i));
        GL_CALL(glVertexAttribPointer(i, element.count, element.type, element.normalized, layout.get_stride(), (const void *)offset));
        offset += element.count * VertexBufferElement::get_type_size(element.type);
    }
}

void VertexArray::bind() const {
    GL_CALL(glBindVertexArray(m_renderer_id));
}

void VertexArray::unbind() const {
    GL_CALL(glBindVertexArray(0));
}
