#include <glew/GL/glew.h>
#include <glm/gtc/type_ptr.hpp>

#include "batch_rendering_color.hpp"

BatchRenderingColor::BatchRenderingColor(const std::string &key, const std::string &name, OrthographicCamera *camera)
    : Test(key, name, camera) {

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    m_shader = new ShaderProgram("assets/shaders/batch-rendering_color.glsl");

    glGenVertexArrays(1, &m_quad_va);
    glBindVertexArray(m_quad_va);

    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, sizeof(float) * 7, 0);

    glEnableVertexAttribArray(1);
    glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, sizeof(float) * 7, (const void *)(sizeof(float) * 3));

    // clang-format off
    uint32_t indices[] = {
        0, 1, 2, 2, 3, 0,
        4, 5, 6, 6, 7, 4
    };
    // clang-format on

    glGenBuffers(1, &m_quad_ib);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_quad_ib);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
}

BatchRenderingColor::~BatchRenderingColor() {
    glDeleteBuffers(1, &m_quad_ib);
    glDeleteBuffers(1, &m_quad_vb);
    glDeleteVertexArrays(1, &m_quad_va);
    delete m_shader;

    glBlendFunc(GL_ONE, GL_ZERO);
    glDisable(GL_BLEND);
    glDisable(GL_DEPTH_TEST);
}

void BatchRenderingColor::on_update(float dt) {
    // clang-format off
    float vertices[] = {
        -150.0f, -50.0f, 0.0f, 0.18f, 0.6f, 0.96f, 1.0f,
         -50.0f, -50.0f, 0.0f, 0.18f, 0.6f, 0.96f, 1.0f,
         -50.0f,  50.0f, 0.0f, 0.18f, 0.6f, 0.96f, 1.0f,
        -150.0f,  50.0f, 0.0f, 0.18f, 0.6f, 0.96f, 1.0f,

          50.0f, -50.0f, 0.0f, 1.0f, 0.93f, 0.24f, 1.0f,
         150.0f, -50.0f, 0.0f, 1.0f, 0.93f, 0.24f, 1.0f,
         150.0f,  50.0f, 0.0f, 1.0f, 0.93f, 0.24f, 1.0f,
          50.0f,  50.0f, 0.0f, 1.0f, 0.93f, 0.24f, 1.0f
    };
    // clang-format on

    glGenBuffers(1, &m_quad_vb);
    glBindBuffer(GL_ARRAY_BUFFER, m_quad_vb);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_DYNAMIC_DRAW);
}

void BatchRenderingColor::on_render() {
    glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glUseProgram(m_shader->get_renderer_id());

    int location = glGetUniformLocation(m_shader->get_renderer_id(), "u_mvp");
    glUniformMatrix4fv(location, 1, GL_FALSE, glm::value_ptr(get_camera()->get_view_projection()));

    glBindVertexArray(m_quad_va);
    glDrawElements(GL_TRIANGLES, 12, GL_UNSIGNED_INT, nullptr);
}

void BatchRenderingColor::on_imgui_render() {
}
