#pragma once

#include <string>
#include <unordered_map>

#include <glm/ext/matrix_float4x4.hpp>

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
  public:
    Shader(const std::string &filepath);
    ~Shader();

    void bind() const;
    void unbind() const;

    inline unsigned int get_renderer_id() const { return m_renderer_id; }

    void set_uniform_1i(const std::string &name, int value);
    void set_uniform_4f(const std::string &name, float v0, float v1, float v2, float v4);
    void set_uniform_mat4f(const std::string &name, const glm::mat4 &matrix);

  private:
    std::string m_filepath;
    unsigned int m_renderer_id;
    std::unordered_map<std::string, int> m_uniform_location_cache;

    unsigned int create_shader();
    ShaderSource parse_shader();
    unsigned int compile_shader(unsigned int type, const std::string &source);
    int get_uniform_location(const std::string &name);
};
