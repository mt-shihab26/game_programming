#include "glew/GL/glew.h"

#include "test_texture_2d.hpp"
#include "core/log.hpp"
#include "opengl/helper.hpp"

TestTexture2D::TestTexture2D(const std::string &key, const std::string &name) : Test(key, name) {
    log_info("Opened test '{}' (key: {})", get_name(), get_key());
}

TestTexture2D::~TestTexture2D() {
    log_info("Closed test '{}' (key: {})", get_name(), get_key());
}

void TestTexture2D::on_update(float dt) {}

void TestTexture2D::on_render() {
    GL_CALL(glClearColor(0.0f, 0.0f, 0.0f, 1.0f));
    GL_CALL(glClear(GL_COLOR_BUFFER_BIT));
}

void TestTexture2D::on_imgui_render() {}
