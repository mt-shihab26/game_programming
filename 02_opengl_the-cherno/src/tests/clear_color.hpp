#pragma once

#include "test.hpp"

namespace test {

class ClearColor : public Test {
  public:
    ClearColor();
    ~ClearColor();

    void on_update(float dt) override;
    void on_render() override;
    void on_imgui_render() override;

  private:
    float m_clear_color[4];
};

} // namespace test
