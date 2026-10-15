#include <string>

#include <glew/GL/glew.h>

#include "core/log.hpp"

#include "helper.hpp"

#include "shader.hpp"

Shader::Shader(const std::string &filepath) : m_program(filepath) {
}

void Shader::bind() const {
    GL_CALL(glUseProgram(get_renderer_id()));
}

void Shader::unbind() const {
    GL_CALL(glUseProgram(0));
}

int Shader::get_uniform_location(const std::string &name) {
    if (m_uniform_location_cache.find(name) != m_uniform_location_cache.end()) {
        return m_uniform_location_cache[name];
    }

    int location;
    GL_CALL(location = glGetUniformLocation(get_renderer_id(), name.c_str()));
    if (location == -1) {
        log_warn("Uniform '{}' doesn't exist", name);
    } else {
        m_uniform_location_cache[name] = location;
    }

    return location;
}

void Shader::set_uniform_1i(const std::string &name, int value) {
    GL_CALL(glUniform1i(get_uniform_location(name), value));
}

void Shader::set_uniform_4f(const std::string &name, float v0, float v1, float v2, float v3) {
    GL_CALL(glUniform4f(get_uniform_location(name), v0, v1, v2, v3));
}

void Shader::set_uniform_mat4f(const std::string &name, const glm::mat4 &matrix) {
    GL_CALL(glUniformMatrix4fv(get_uniform_location(name), 1, GL_FALSE, &matrix[0][0]));
}
