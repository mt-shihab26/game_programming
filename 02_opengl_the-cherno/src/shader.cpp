#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

#include "path.hpp"
#include "shader.hpp"

#include <GL/glew.h>
#include <GLFW/glfw3.h>

unsigned int create_shader(std::string filepath) {
    ShaderSource shader_source = parse_shader(filepath);

    unsigned int program = glCreateProgram();

    unsigned int vs = compile_shader(GL_VERTEX_SHADER, shader_source.vertex);
    unsigned int fs = compile_shader(GL_FRAGMENT_SHADER, shader_source.fragment);

    glAttachShader(program, vs);
    glAttachShader(program, fs);

    glLinkProgram(program);
    glValidateProgram(program);

    glDeleteShader(vs);
    glDeleteShader(fs);

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

    unsigned int id = glCreateShader(type);
    glShaderSource(id, 1, &src, nullptr);
    glCompileShader(id);

    // error handling
    int result;
    glGetShaderiv(id, GL_COMPILE_STATUS, &result);
    if (!result) {
        int length;
        glGetShaderiv(id, GL_INFO_LOG_LENGTH, &length);
        char *message = (char *)alloca(length * sizeof(char));
        glGetShaderInfoLog(id, length, &length, message);
        std::cout << "Failed to compile " << (type == GL_VERTEX_SHADER ? "vertex" : "fragment") << " shader!" << std::endl;
        std::cout << message << std::endl;
        glDeleteShader(id);
        return 0;
    }

    return id;
}
