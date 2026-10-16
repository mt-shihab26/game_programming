#include <glew/GL/glew.h>

#include "core/log.hpp"

#include "debug.hpp"
#include "helper.hpp"

static DebugLogLevel s_debug_log_level = DebugLogLevel::HighAssert;

void set_gl_debug_log_level(DebugLogLevel level) {
    s_debug_log_level = level;
}

// OpenGL calls this itself whenever the driver has something to report
static void GLAPIENTRY gl_log_message(GLenum source, GLenum type, GLuint id, GLenum severity, GLsizei length,
                                      const GLchar *message, const void *user_param) {
    switch (severity) {
    case GL_DEBUG_SEVERITY_HIGH:
        if ((int)s_debug_log_level > 0) {
            log_error("[OpenGL Debug HIGH] {}", message);
            if (s_debug_log_level == DebugLogLevel::HighAssert) {
                ASSERT(false);
            }
        }
        break;
    case GL_DEBUG_SEVERITY_MEDIUM:
        if ((int)s_debug_log_level > 2) {
            log_warn("[OpenGL Debug MEDIUM] {}", message);
        }
        break;
    case GL_DEBUG_SEVERITY_LOW:
        if ((int)s_debug_log_level > 3) {
            log_info("[OpenGL Debug LOW] {}", message);
        }
        break;
    case GL_DEBUG_SEVERITY_NOTIFICATION:
        if ((int)s_debug_log_level > 4) {
            log_info("[OpenGL Debug NOTIFICATION] {}", message);
        }
        break;
    }
}

void enable_gl_debugging() {
    glDebugMessageCallback(gl_log_message, nullptr);
    glEnable(GL_DEBUG_OUTPUT);
    // report the error inside the GL call that caused it, so a breakpoint shows the right line
    glEnable(GL_DEBUG_OUTPUT_SYNCHRONOUS);
    // ShaderProgram reports compile errors itself, with the shader file name
    glDebugMessageControl(GL_DEBUG_SOURCE_SHADER_COMPILER, GL_DONT_CARE, GL_DONT_CARE, 0, nullptr, GL_FALSE);
}
