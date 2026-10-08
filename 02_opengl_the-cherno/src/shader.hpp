#pragma once

#include <string>

enum ShaderType {
    None = -1,
    Vertex = 0,
    Fragment = 1,
};

struct ShaderSource {
    std::string vertex;
    std::string fragment;
};

static unsigned int create_shader(ShaderSource &shader_source);
static unsigned int compile_shader(unsigned int type, const std::string &source);
ShaderSource parse_shader(std::string $filepath);
