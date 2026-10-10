#pragma once

#include <vector>

#include <GL/glew.h>

#include "renderer.hpp"

struct VertexBufferElement {
    unsigned int type;
    unsigned int count;
    unsigned char normalized;

    static unsigned int get_type_size(unsigned int type) {
        switch (type) {
        case GL_FLOAT:
            return 4;
        case GL_UNSIGNED_INT:
            return 4;
        case GL_UNSIGNED_BYTE:
            return 1;
        }
        ASSERT(false);
        return 0;
    }
};

class VertexBufferLayout {
  private:
    std::vector<VertexBufferElement> m_elements;
    unsigned int m_stride;

  public:
    VertexBufferLayout() : m_stride(0) {};

    template <typename T>
    void push(unsigned int count) = delete;

    template <>
    void push<float>(unsigned int count);

    template <>
    void push<unsigned int>(unsigned int count);

    template <>
    void push<unsigned char>(unsigned int count);

    inline unsigned int get_stride() const { return m_stride; }
    inline const std::vector<VertexBufferElement> &get_elements() const { return m_elements; }
};
