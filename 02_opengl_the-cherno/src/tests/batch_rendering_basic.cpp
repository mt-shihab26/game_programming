#include <glew/GL/glew.h>
#include <glm/gtc/type_ptr.hpp>

#include "core/test.hpp"

#include "batch_rendering_basic.hpp"

BatchRenderingBasic::BatchRenderingBasic(const std::string &key, const std::string &name, OrthographicCamera *camera)
    : Test(key, name, camera) {

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    m_shader = new Shader("assets/shaders/batch-rendering_basic.glsl");

    glGenVertexArrays(1, &m_quad_va);
    glBindVertexArray(m_quad_va);

    float vertices[] = {
        -0.5f, -0.5f, 0.0f,
        0.5f, -0.5f, 0.0f,
        0.5f, 0.5f, 0.0f,
        -0.5f, 0.5f, 0.0f};

    glGenBuffers(1, &m_quad_vb);
    glBindBuffer(GL_ARRAY_BUFFER, m_quad_vb);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, sizeof(float) * 3, 0);

    uint32_t indices[] = {0, 1, 2, 2, 3, 0};
    glGenBuffers(1, &m_quad_ib);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_quad_ib);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
}

BatchRenderingBasic::~BatchRenderingBasic() {
    glDeleteBuffers(1, &m_quad_ib);
    glDeleteBuffers(1, &m_quad_vb);
    glDeleteVertexArrays(1, &m_quad_va);
    delete m_shader;
}

void BatchRenderingBasic::on_update(float dt) {
    glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glUseProgram(m_shader->get_renderer_id());

    int location = glGetUniformLocation(m_shader->get_renderer_id(), "u_mvp");
    glUniformMatrix4fv(location, 1, GL_FALSE, glm::value_ptr(get_camera()->get_view_projection()));

    glBindVertexArray(m_quad_va);
}

void BatchRenderingBasic::on_render() {
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, nullptr);
}

void BatchRenderingBasic::on_imgui_render() {
}
