#pragma once

#include "test.hpp"

namespace test {

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

} // namespace test
