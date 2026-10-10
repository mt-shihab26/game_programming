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

  public:
    VertexBufferLayout() = default;

    template <typename T>
    void push(unsigned int count) = delete;

    template <>
    void push<float>(unsigned int count);

    template <>
    void push<unsigned int>(unsigned int count);

    template <>
    void push<unsigned char>(unsigned int count);
};

