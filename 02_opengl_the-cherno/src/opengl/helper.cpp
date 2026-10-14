#include <glew/GL/glew.h>

#include "core/log.hpp"

#include "helper.hpp"

void gl_clear_error() {
    while (glGetError() != GL_NO_ERROR) {
    }
}

bool gl_log_call(const char *function, const char *file, int line) {
    while (GLenum error = glGetError()) {
        log_error("OpenGL error {} in {} at {}:{}", error, function, file, line);
        return false;
    }
    return true;
}
