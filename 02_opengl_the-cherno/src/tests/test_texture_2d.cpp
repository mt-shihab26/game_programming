#include <glew/GL/glew.h>
#include <glm/ext/matrix_clip_space.hpp>
#include <glm/ext/matrix_transform.hpp>
#include <glm/ext/vector_float3.hpp>
#include <glm/glm.hpp>
#include <imgui/imgui.h>
#include <imgui/imgui_impl_glfw.h>
#include <imgui/imgui_impl_opengl3.h>

#include "core/log.hpp"
#include "opengl/helper.hpp"
#include "opengl/index_buffer.hpp"
#include "opengl/renderer.hpp"
#include "opengl/shader.hpp"
#include "opengl/texture.hpp"
#include "opengl/vertex_array.hpp"
#include "opengl/vertex_buffer.hpp"

#include "test_texture_2d.hpp"

TestTexture2D::TestTexture2D(const std::string &key, const std::string &name)
    : Test(key, name), m_vertex_buffer(m_positions, sizeof(m_positions)), m_index_buffer(m_indices, 6),
      m_shader("assets/shaders/basic.glsl"), m_texture("assets/textures/omarchy-logo-tokyo-night.png") {

    log_info("Opened test '{}' (key: {})", get_name(), get_key());

    GL_CALL(glEnable(GL_BLEND));
    GL_CALL(glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA));

    VertexBufferLayout layout;
    layout.push<float>(2);
    layout.push<float>(2);
    m_vertex_array.add_buffer(m_vertex_buffer, layout);

    m_view = glm::translate(glm::mat4(1.0f), glm::vec3(0, 0, 0));
    m_translation = glm::vec3(200, 200, 0);

    m_shader.bind();
    m_shader.set_uniform_1i("u_texture", 0);

    m_texture.bind();

    m_vertex_array.unbind();
    m_shader.unbind();
    m_vertex_buffer.unbind();
    m_index_buffer.unbind();
}

TestTexture2D::~TestTexture2D() {
    GL_CALL(glBlendFunc(GL_ONE, GL_ZERO));
    GL_CALL(glDisable(GL_BLEND));

    log_info("Closed test '{}' (key: {})", get_name(), get_key());
}

void TestTexture2D::on_update(float dt) {
}

void TestTexture2D::on_render() {
    ImGuiIO &io = ImGui::GetIO();

    m_projection = glm::ortho(0.0f, io.DisplaySize.x, 0.0f, io.DisplaySize.y, -1.0f, 1.0f);

    glm::mat4 model = glm::translate(glm::mat4(1.0), m_translation);
    glm::mat4 mvp = m_projection * m_view * model;

    m_shader.bind();
    m_shader.set_uniform_mat4f("u_mvp", mvp);

    m_renderer.draw(m_vertex_array, m_index_buffer, m_shader);
}

void TestTexture2D::on_imgui_render() {
    ImGuiIO &io = ImGui::GetIO();

    ImGui::SliderFloat3("Translation", &m_translation.x, 0.0f, io.DisplaySize.x);
}
