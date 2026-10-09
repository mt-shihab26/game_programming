#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

#include "error.hpp"
#include "path.hpp"
#include "shader.hpp"

#include <GL/glew.h>
#include <GLFW/glfw3.h>

unsigned int create_shader(std::string filepath) {
    ShaderSource shader_source = parse_shader(filepath);

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

ShaderSource parse_shader(std::string filepath) {
    std::ifstream stream(project_path(filepath));

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

unsigned int compile_shader(unsigned int type, const std::string &source) {
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
