#include <GL/glew.h>

#include "helper.hpp"
#include "renderer.hpp"

void Renderer::draw(const VertexArray &va, const IndexBuffer &ib, const Shader &shader) const {
    va.bind();
    ib.bind();
    shader.bind();

    GL_CALL(glDrawElements(GL_TRIANGLES, ib.get_count(), GL_UNSIGNED_INT, nullptr));
}
