#include <stdexcept>

#include <glew/GL/glew.h>
#include <glfw/GLFW/glfw3.h>

#include "log.hpp"
#include "opengl_layer.hpp"

// OpenGL and GLEW return strings as unsigned char, std::format needs const char
static const char *gl_string(const unsigned char *string) {
    return reinterpret_cast<const char *>(string);
}

static void print_library_versions() {
    log_info("Vendor:   {}", gl_string(glGetString(GL_VENDOR)));
    log_info("Renderer: {}", gl_string(glGetString(GL_RENDERER)));
    log_info("OpenGL:   {}", gl_string(glGetString(GL_VERSION)));
    log_info("GLSL:     {}", gl_string(glGetString(GL_SHADING_LANGUAGE_VERSION)));
    log_info("GLEW:     {}", gl_string(glewGetString(GLEW_VERSION)));
    log_info("GLFW:     {}", glfwGetVersionString());
}

OpenGLLayer::OpenGLLayer() {
    if (glewInit() != GLEW_OK) {
        throw std::runtime_error("failed to initialise GLEW");
    }
    print_library_versions();
}

void OpenGLLayer::begin_frame() const {
    m_renderer.clear();
}
