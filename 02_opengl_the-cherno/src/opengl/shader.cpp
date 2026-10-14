#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

#include <glew/GL/glew.h>

#include "core/path.hpp"

#include "helper.hpp"

#include "shader.hpp"

unsigned int Shader::create_shader() {
    ShaderSource shader_source = parse_shader();

    unsigned int program;
    GL_CALL(program = glCreateProgram());

    unsigned int vs = compile_shader(GL_VERTEX_SHADER, shader_source.vertex);
    unsigned int fs = compile_shader(GL_FRAGMENT_SHADER, shader_source.fragment);

    GL_CALL(glAttachShader(program, vs));
    GL_CALL(glAttachShader(program, fs));

    GL_CALL(glLinkProgram(program));

    int linked;
    GL_CALL(glGetProgramiv(program, GL_LINK_STATUS, &linked));
    if (!linked) {
        int length;
        GL_CALL(glGetProgramiv(program, GL_INFO_LOG_LENGTH, &length));
        char *message = (char *)alloca(length * sizeof(char));
        GL_CALL(glGetProgramInfoLog(program, length, &length, message));
        std::cout << "Failed to link shader program!" << std::endl;
        std::cout << message << std::endl;
    }

    GL_CALL(glValidateProgram(program));

    GL_CALL(glDeleteShader(vs));
    GL_CALL(glDeleteShader(fs));

    return program;
}

ShaderSource Shader::parse_shader() {
    std::ifstream stream(project_path(m_filepath));
    if (!stream) {
        std::cout << "Failed to open shader '" << project_path(m_filepath) << "'" << std::endl;
    }

    std::string line;
    std::stringstream ss[2];
    ShaderType type = ShaderType::None;

    while (getline(stream, line)) {
        if (line.find("#type") != std::string::npos) {
            if (line.find("vertex") != std::string::npos) {
                type = ShaderType::Vertex;
            }
            if (line.find("fragment") != std::string::npos) {
                type = ShaderType::Fragment;
            }
        } else if (type != ShaderType::None) {
            // lines before the first #type don't belong to any shader
            ss[(int)type] << line << "\n";
        }
    }

    return {ss[0].str(), ss[1].str()};
}

unsigned int Shader::compile_shader(unsigned int type, const std::string &source) {
    const char *src = source.c_str();

    unsigned int id;
    GL_CALL(id = glCreateShader(type));
    GL_CALL(glShaderSource(id, 1, &src, nullptr));
    GL_CALL(glCompileShader(id));

    // error handling
    int result;
    GL_CALL(glGetShaderiv(id, GL_COMPILE_STATUS, &result));
    if (!result) {
        int length;
        GL_CALL(glGetShaderiv(id, GL_INFO_LOG_LENGTH, &length));
        char *message = (char *)alloca(length * sizeof(char));
        GL_CALL(glGetShaderInfoLog(id, length, &length, message));
        std::cout << "Failed to compile " << (type == GL_VERTEX_SHADER ? "vertex" : "fragment") << " shader!" << std::endl;
        std::cout << message << std::endl;
        GL_CALL(glDeleteShader(id));
        return 0;
    }

    return id;
}

int Shader::get_uniform_location(const std::string &name) {
    if (m_uniform_location_cache.find(name) != m_uniform_location_cache.end()) {
        return m_uniform_location_cache[name];
    }

    int location;
    GL_CALL(location = glGetUniformLocation(m_renderer_id, name.c_str()));
    if (location == -1) {
        std::cout << "Warning: uniform '" << name << "'doesn't exist!" << std::endl;
    } else {
        m_uniform_location_cache[name] = location;
    }
    return location;
}

Shader::Shader(const std::string &filepath) : m_filepath(filepath), m_renderer_id(0) {
    m_renderer_id = create_shader();
}

Shader::~Shader() {
    GL_CALL(glDeleteProgram(m_renderer_id));
}

void Shader::bind() const {
    GL_CALL(glUseProgram(m_renderer_id));
}

void Shader::unbind() const {
    GL_CALL(glUseProgram(0));
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
