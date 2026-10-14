#pragma once

#include "core/test.hpp"

class TestClearColor : public Test {
  public:
    TestClearColor();
    ~TestClearColor();

    void on_update(float dt) override;
    void on_render() override;
    void on_imgui_render() override;

  private:
    float m_clear_color[4];
};
