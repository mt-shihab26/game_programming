#pragma once

#include "core/test.hpp"
#include "opengl/orthographic_camera.hpp"
#include "opengl/shader_program.hpp"
#include <glew/GL/glew.h>

class BatchRenderingTexture : public Test {
  public:
    BatchRenderingTexture(const std::string &key, const std::string &name, OrthographicCamera *camera);
    ~BatchRenderingTexture();

    void on_update(float dt) override;
    void on_render() override;
    void on_imgui_render() override;

  private:
    ShaderProgram *m_shader;

    GLuint m_quad_va, m_quad_vb, m_quad_ib;
    GLuint m_texture_a;
    GLuint m_texture_b;

    glm::vec4 color_a{0.18f, 0.6f, 0.96f, 1.0f};
    glm::vec4 color_b{1.0f, 0.93f, 0.24f, 1.0f};
};
