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

ShaderSource parse_shader(std::string $filepath);
