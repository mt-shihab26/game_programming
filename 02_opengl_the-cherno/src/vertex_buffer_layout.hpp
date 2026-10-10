#pragma once

#include <GL/glew.h>
#include <vector>

struct VertexBufferElement {
    unsigned int type;
    unsigned int count;
    bool normalized;
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
    inline const std::vector<VertexBufferElement> get_elements() { return m_elements; }
};
