#pragma once

#include <string>

class Test {
  public:
    Test(const std::string &key, const std::string &name) : m_key(key), m_name(name) {}
    virtual ~Test() {}

    virtual void on_update(float dt) {}
    virtual void on_render() {}
    virtual void on_imgui_render() {}

    const std::string &get_key() const { return m_key; }
    const std::string &get_name() const { return m_name; }

  private:
    std::string m_key;
    std::string m_name;
};
