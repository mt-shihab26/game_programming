#include <cstdio>
#include <stdexcept>

#include <glew/GL/glew.h>
#include <glfw/GLFW/glfw3.h>

#include "opengl/helper.hpp"
#include "opengl_layer.hpp"

static void print_library_versions() {
    GL_CALL(printf("Vendor:   %s\n", glGetString(GL_VENDOR)));
    GL_CALL(printf("Renderer: %s\n", glGetString(GL_RENDERER)));
    GL_CALL(printf("OpenGL:   %s\n", glGetString(GL_VERSION)));
    GL_CALL(printf("GLSL:     %s\n", glGetString(GL_SHADING_LANGUAGE_VERSION)));
    printf("GLEW:     %s\n", glewGetString(GLEW_VERSION));
    printf("GLFW:     %s\n", glfwGetVersionString());
}

OpenGLLayer::OpenGLLayer() {
    if (glewInit() != GLEW_OK) {
        throw std::runtime_error("failed to initialise GLEW");
    }

    print_library_versions();

    GL_CALL(glEnable(GL_BLEND));
    GL_CALL(glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA));
}

void OpenGLLayer::begin_frame() const {
    m_renderer.clear();
}
