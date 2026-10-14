#pragma once

#include <string>

namespace test {

class Test {
  public:
    Test() {}
    virtual ~Test() {}

    virtual void on_update(float dt) {}
    virtual void on_render() {}
    virtual void on_imgui_render() {}

    const std::string &get_name() const { return *m_name; }
    void set_name(const std::string &name) { m_name = &name; }

  private:
    const std::string *m_name = nullptr;
};
} // namespace test
