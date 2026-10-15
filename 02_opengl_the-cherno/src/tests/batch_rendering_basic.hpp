#pragma once

#include "core/test.hpp"
#include "opengl/orthographic_camera.hpp"
#include "opengl/shader.hpp"
#include <glew/GL/glew.h>

class BatchRenderingBasic : public Test {
  public:
    BatchRenderingBasic(const std::string &key, const std::string &name, OrthographicCamera *camera);
    ~BatchRenderingBasic();

    void on_update(float dt) override;
    void on_render() override;
    void on_imgui_render() override;

  private:
    Shader *m_shader;

    GLuint m_quad_va, m_quad_vb, m_quad_ib;
};
