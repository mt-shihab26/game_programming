#pragma once

#include "opengl/orthographic_camera.hpp"
#include <string>

class Test {
  public:
    Test(const std::string &key, const std::string &name, const OrthographicCamera camera)
        : m_key(key), m_name(name), m_camera(camera) {}
    virtual ~Test() {}

    virtual void on_update(float dt) {}
    virtual void on_render() {}
    virtual void on_imgui_render() {}

    const std::string &get_key() const { return m_key; }
    const std::string &get_name() const { return m_name; }
    const OrthographicCamera &get_camera() const { return m_camera; }

  private:
    std::string m_key;
    std::string m_name;
    OrthographicCamera m_camera;
};
