#include <fstream>
#include <iostream>
#include <ostream>
#include <sstream>
#include <string>

#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include "renderer.hpp"
#include "path.hpp"
#include "shader.hpp"

unsigned int Shader::create_shader() {
    ShaderSource shader_source = parse_shader();

    GL_CALL(unsigned int program = glCreateProgram());

    unsigned int vs = compile_shader(GL_VERTEX_SHADER, shader_source.vertex);
    unsigned int fs = compile_shader(GL_FRAGMENT_SHADER, shader_source.fragment);

    GL_CALL(glAttachShader(program, vs));
    GL_CALL(glAttachShader(program, fs));

    GL_CALL(glLinkProgram(program));
    GL_CALL(glValidateProgram(program));

    GL_CALL(glDeleteShader(vs));
    GL_CALL(glDeleteShader(fs));

    return program;
}

ShaderSource Shader::parse_shader() {
    std::ifstream stream(project_path(m_filepath));

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
        } else {
            ss[(int)type] << line << "\n";
        }
    }

    return {ss[0].str(), ss[1].str()};
}

unsigned int Shader::compile_shader(unsigned int type, const std::string &source) {
    const char *src = source.c_str();

    GL_CALL(unsigned int id = glCreateShader(type));
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

unsigned int Shader::get_uniform_location(const std::string &name) {
    GL_CALL(int location = glGetUniformLocation(m_renderer_id, name.c_str()));
    if (location == -1) {
        std::cout << "Warning: uniform '" << name << "'doesn't exist!" << std::endl;
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

void Shader::set_uniform_4f(const std::string &name, float v0, float v1, float v2, float v3) {
    GL_CALL(glUniform4f(get_uniform_location(name), v0, v1, v2, v3));
}
