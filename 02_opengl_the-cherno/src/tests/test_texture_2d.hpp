#pragma once

#include <glm/glm.hpp>

#include "core/test.hpp"
#include "opengl/index_buffer.hpp"
#include "opengl/orthographic_camera.hpp"
#include "opengl/renderer.hpp"
#include "opengl/shader.hpp"
#include "opengl/texture.hpp"
#include "opengl/vertex_array.hpp"
#include "opengl/vertex_buffer.hpp"

class TestTexture2D : public Test {
  public:
    TestTexture2D(const std::string &key, const std::string &name, OrthographicCamera *camera);
    ~TestTexture2D();

    void on_update(float dt) override;
    void on_render() override;
    void on_imgui_render() override;

  private:
    // clang-format off
    float m_positions[16] = {
        -50.0f, -50.0f, 0.0f, 0.0f, // 0
         50.0f, -50.0f, 1.0f, 0.0f, // 1
         50.0f,  50.0f, 1.0f, 1.0f, // 2
        -50.0f,  50.0f, 0.0f, 1.0f  // 3
    };

    unsigned int m_indices[6] = {
        0, 1, 2,
        2, 3, 0
    };
    // clang-format on

    VertexArray m_vertex_array;
    VertexBuffer m_vertex_buffer;
    IndexBuffer m_index_buffer;
    Shader m_shader;
    Texture m_texture;
    Renderer m_renderer;

    glm::mat4 m_projection;
    glm::mat4 m_view;
    glm::vec3 m_translation;
};
