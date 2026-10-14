#include <glew/GL/glew.h>
#include <glm/glm.hpp>
#include "glm/ext/matrix_clip_space.hpp"
#include "glm/ext/matrix_transform.hpp"
#include "glm/ext/vector_float3.hpp"

#include "core/log.hpp"
#include "opengl/helper.hpp"
#include "opengl/vertex_array.hpp"
#include "opengl/vertex_buffer.hpp"
#include "opengl/index_buffer.hpp"
#include "opengl/shader.hpp"
#include "opengl/texture.hpp"

#include "test_texture_2d.hpp"

TestTexture2D::TestTexture2D(const std::string &key, const std::string &name) : Test(key, name) {
    log_info("Opened test '{}' (key: {})", get_name(), get_key());
}

TestTexture2D::~TestTexture2D() {
    log_info("Closed test '{}' (key: {})", get_name(), get_key());
}

void TestTexture2D::on_update(float dt) {
}

void TestTexture2D::on_render() {
}

void TestTexture2D::on_imgui_render() {
}
