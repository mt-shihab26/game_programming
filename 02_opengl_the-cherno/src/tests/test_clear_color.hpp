#pragma once

#include "core/test.hpp"

class TestClearColor : public Test {
  public:
    TestClearColor(const std::string &key, const std::string &name);
    ~TestClearColor();

    void on_render() override;
    void on_imgui_render() override;

  private:
    float m_clear_color[4];
};
