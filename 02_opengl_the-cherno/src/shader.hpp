#pragma once

#include <string>
#include <unordered_map>

enum ShaderType {
    None = -1,
    Vertex = 0,
    Fragment = 1,
};

struct ShaderSource {
    std::string vertex;
    std::string fragment;
};

class Shader {
  private:
    std::string m_filepath;
    unsigned int m_renderer_id;
    std::unordered_map<std::string, unsigned int> m_uniform_location_cache;

    unsigned int create_shader();
    ShaderSource parse_shader();
    unsigned int compile_shader(unsigned int type, const std::string &source);
    unsigned int get_uniform_location(const std::string &name);

  public:
    Shader(const std::string &filepath);
    ~Shader();

    void bind() const;
    void unbind() const;

    void set_uniform_4f(const std::string &name, float v0, float v1, float v2, float v4);
};
