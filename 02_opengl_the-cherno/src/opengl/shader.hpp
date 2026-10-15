#pragma once

#include <string>
#include <unordered_map>

#include <glm/ext/matrix_float4x4.hpp>

#include "basic_shader.hpp"

class Shader {
  public:
    Shader(const std::string &filepath);

    void bind() const;
    void unbind() const;

    inline unsigned int get_renderer_id() const { return m_program.get_renderer_id(); }

    void set_uniform_1i(const std::string &name, int value);
    void set_uniform_4f(const std::string &name, float v0, float v1, float v2, float v4);
    void set_uniform_mat4f(const std::string &name, const glm::mat4 &matrix);

  private:
    BasicShader m_program;
    std::unordered_map<std::string, int> m_uniform_location_cache;

    int get_uniform_location(const std::string &name);
};
