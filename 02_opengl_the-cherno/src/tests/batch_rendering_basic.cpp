#include <glew/GL/glew.h>

#include "core/test.hpp"

#include "batch_rendering_basic.hpp"

BatchRenderingBasic::BatchRenderingBasic(const std::string &key, const std::string &name, OrthographicCamera *camera)
    : Test(key, name, camera) {

    EnableGLDebugging();

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    m_shader = new Shader("assets/shaders/texture.glsl");

    glCreateVertexArrays(1, &m_QuadVA);
    glBindVertexArray(m_QuadVA);

    float vertices[] = {
        -0.5f, -0.5f, 0.0f,
        0.5f, -0.5f, 0.0f,
        0.5f, 0.5f, 0.0f,
        -0.5f, 0.5f, 0.0f};

    glCreateBuffers(1, &m_QuadVB);
    glBindBuffer(GL_ARRAY_BUFFER, m_QuadVB);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, sizeof(float) * 3, 0);

    uint32_t indices[] = {0, 1, 2, 2, 3, 0};
    glCreateBuffers(1, &m_QuadIB);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_QuadIB);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
}

BatchRenderingBasic::~BatchRenderingBasic() {
}

void BatchRenderingBasic::on_update(float dt) {
}

void BatchRenderingBasic::on_render() {
}

void BatchRenderingBasic::on_imgui_render() {
}
