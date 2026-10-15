#include <fstream>
#include <sstream>
#include <string>

#include <glew/GL/glew.h>

#include "core/log.hpp"
#include "core/path.hpp"

#include "shader_program.hpp"

static GLuint compile_shader(GLenum type, const std::string &source) {
    const char *src = source.c_str();

    GLuint id = glCreateShader(type);
    glShaderSource(id, 1, &src, nullptr);
    glCompileShader(id);

    GLint compiled;
    glGetShaderiv(id, GL_COMPILE_STATUS, &compiled);
    if (!compiled) {
        char message[1024];
        glGetShaderInfoLog(id, sizeof(message), nullptr, message);
        log_error("Failed to compile {} shader:\n{}", type == GL_VERTEX_SHADER ? "vertex" : "fragment", message);
    }

    return id;
}

ShaderProgram::ShaderProgram(const std::string &filepath) {
    std::ifstream stream(project_path(filepath));
    if (!stream) {
        log_error("Failed to open shader '{}'", project_path(filepath));
    }

    // index 0 collects vertex lines, 1 collects fragment lines
    std::stringstream sources[2];
    int current = -1;

    std::string line;
    while (getline(stream, line)) {
        if (line.find("#type vertex") != std::string::npos) {
            current = 0;
        } else if (line.find("#type fragment") != std::string::npos) {
            current = 1;
        } else if (current != -1) {
            sources[current] << line << "\n";
        }
    }

    GLuint vs = compile_shader(GL_VERTEX_SHADER, sources[0].str());
    GLuint fs = compile_shader(GL_FRAGMENT_SHADER, sources[1].str());

    m_renderer_id = glCreateProgram();
    glAttachShader(m_renderer_id, vs);
    glAttachShader(m_renderer_id, fs);
    glLinkProgram(m_renderer_id);

    GLint linked;
    glGetProgramiv(m_renderer_id, GL_LINK_STATUS, &linked);
    if (!linked) {
        char message[1024];
        glGetProgramInfoLog(m_renderer_id, sizeof(message), nullptr, message);
        log_error("Failed to link shader '{}':\n{}", filepath, message);
    }

    // the program keeps its own copy once linked
    glDeleteShader(vs);
    glDeleteShader(fs);
}

ShaderProgram::~ShaderProgram() {
    glDeleteProgram(m_renderer_id);
}
