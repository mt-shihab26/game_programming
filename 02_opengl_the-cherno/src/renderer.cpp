#include <glew/GL/glew.h>

#include "supports/helper.hpp"

#include "renderer.hpp"

void Renderer::clear() const {
    GL_CALL(glClear(GL_COLOR_BUFFER_BIT));
}

void Renderer::draw(const VertexArray &va, const IndexBuffer &ib, const Shader &shader) const {
    va.bind();
    ib.bind();
    shader.bind();

    GL_CALL(glClearColor(0.0f, 0.0f, 0.0f, 1.0f));
    GL_CALL(glDrawElements(GL_TRIANGLES, ib.get_count(), GL_UNSIGNED_INT, nullptr));
}
