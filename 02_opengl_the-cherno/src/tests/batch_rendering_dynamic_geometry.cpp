#include <array>
#include <cstddef>
#include <string>

#include <glew/GL/glew.h>
#include <glm/gtc/type_ptr.hpp>
#include <stb/stb_image.h>

#include "core/log.hpp"
#include "core/path.hpp"

#include "batch_rendering_dynamic_geometry.hpp"

static GLuint load_texture(const std::string &path) {
    int w, h, bits;

    stbi_set_flip_vertically_on_load(1);
    auto pixels = stbi_load(project_path(path).c_str(), &w, &h, &bits, STBI_rgb_alpha);

    GLuint texture_id;
    glCreateTextures(GL_TEXTURE_2D, 1, &texture_id);
    glBindTexture(GL_TEXTURE_2D, texture_id);
    glBindTexture(GL_TEXTURE_2D, texture_id);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, pixels);

    stbi_image_free(pixels);

    return texture_id;
}

struct Vertex {
    float position[3];
    float tex_coords[2];
    float tex_id;
};

static std::array<Vertex, 4> create_quad(float x, float y, float size, float texture_id) {
    Vertex v0 = {{x, y, 0.0f}, {0.0f, 0.0f}, texture_id};
    Vertex v1 = {{x + size, y, 0.0f}, {1.0f, 0.0f}, texture_id};
    Vertex v2 = {{x + size, y + size, 0.0f}, {1.0f, 1.0f}, texture_id};
    Vertex v3 = {{x, y + size, 0.0f}, {0.0f, 1.0f}, texture_id};

    return {v0, v1, v2, v3};
}

BatchRenderingDynamicGeometry::BatchRenderingDynamicGeometry(const std::string &key, const std::string &name, OrthographicCamera *camera)
    : Test(key, name, camera) {
    log_info("Opened test '{}' (key: {})", get_name(), get_key());

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    m_shader = new ShaderProgram("assets/shaders/batch-rendering-dynamic-geometry.glsl");

    glGenVertexArrays(1, &m_quad_va);
    glBindVertexArray(m_quad_va);

    glGenBuffers(1, &m_quad_vb);
    glBindBuffer(GL_ARRAY_BUFFER, m_quad_vb);
    glBufferData(GL_ARRAY_BUFFER, sizeof(Vertex) * 1000, nullptr, GL_DYNAMIC_DRAW);

    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, sizeof(Vertex), (const void *)(offsetof(Vertex, position)));

    glEnableVertexAttribArray(2);
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, sizeof(Vertex), (const void *)(offsetof(Vertex, tex_coords)));

    glEnableVertexAttribArray(3);
    glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, sizeof(Vertex), (const void *)(offsetof(Vertex, tex_id)));

    // clang-format off
    uint32_t indices[] = {
        0, 1, 2, 2, 3, 0,
        4, 5, 6, 6, 7, 4
    };
    // clang-format on

    glGenBuffers(1, &m_quad_ib);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, m_quad_ib);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

    m_texture_a = load_texture("assets/textures/omarchy-logo-tokyo-night.png");
    m_texture_b = load_texture("assets/textures/raylib-logo.png");
}

BatchRenderingDynamicGeometry::~BatchRenderingDynamicGeometry() {
    glDeleteTextures(1, &m_texture_a);
    glDeleteTextures(1, &m_texture_b);
    glDeleteBuffers(1, &m_quad_ib);
    glDeleteBuffers(1, &m_quad_vb);
    glDeleteVertexArrays(1, &m_quad_va);
    delete m_shader;

    glBlendFunc(GL_ONE, GL_ZERO);
    glDisable(GL_BLEND);
    glDisable(GL_DEPTH_TEST);

    log_info("Closed test '{}' (key: {})", get_name(), get_key());
}

void BatchRenderingDynamicGeometry::on_update(float dt) {
    // clang-format off
    float vertices[] = {
        -150.0f, -50.0f, 0.0f, 0.0f, 0.0f, 0.0f,
         -50.0f, -50.0f, 0.0f, 1.0f, 0.0f, 0.0f,
         -50.0f,  50.0f, 0.0f, 1.0f, 1.0f, 0.0f,
        -150.0f,  50.0f, 0.0f, 0.0f, 1.0f, 0.0f,

          50.0f, -50.0f, 0.0f, 0.0f, 0.0f, 1.0f,
         150.0f, -50.0f, 0.0f, 1.0f, 0.0f, 1.0f,
         150.0f,  50.0f, 0.0f, 1.0f, 1.0f, 1.0f,
          50.0f,  50.0f, 0.0f, 0.0f, 1.0f, 1.0f
    };
    // clang-format on

    glBindBuffer(GL_ARRAY_BUFFER, m_quad_vb);
    glBufferSubData(GL_ARRAY_BUFFER, 0, sizeof(vertices), vertices);
}

void BatchRenderingDynamicGeometry::on_render() {
    glClearColor(0.1f, 0.1f, 0.1f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glUseProgram(m_shader->get_renderer_id());

    int location = glGetUniformLocation(m_shader->get_renderer_id(), "u_mvp");
    glUniformMatrix4fv(location, 1, GL_FALSE, glm::value_ptr(get_camera()->get_view_projection()));

    location = glGetUniformLocation(m_shader->get_renderer_id(), "u_texture");
    int samplers[2] = {0, 1};
    glUniform1iv(location, 2, samplers);

    glBindTextureUnit(0, m_texture_a);
    glBindTextureUnit(1, m_texture_b);

    glBindVertexArray(m_quad_va);
    glDrawElements(GL_TRIANGLES, 12, GL_UNSIGNED_INT, nullptr);
}

void BatchRenderingDynamicGeometry::on_imgui_render() {
}
