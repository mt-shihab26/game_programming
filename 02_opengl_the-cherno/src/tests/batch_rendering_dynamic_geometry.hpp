#pragma once

#include "core/test.hpp"
#include "opengl/orthographic_camera.hpp"
#include "opengl/shader_program.hpp"
#include <glew/GL/glew.h>

struct Vertex {
    float position[3];
    float tex_coords[2];
    float tex_id;
};

class BatchRenderingDynamicGeometry : public Test {
  public:
    BatchRenderingDynamicGeometry(const std::string &key, const std::string &name, OrthographicCamera *camera);
    ~BatchRenderingDynamicGeometry();

    void on_update(float dt) override;
    void on_render() override;
    void on_imgui_render() override;

  private:
    ShaderProgram *m_shader;

    GLuint m_quad_va, m_quad_vb, m_quad_ib;
    GLuint m_texture_a;
    GLuint m_texture_b;

    float m_quad_a_position[2] = {-150.0f, -50.0f};
    float m_quad_b_position[2] = {50.0f, -50.0f};
};
