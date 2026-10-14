#pragma once

#include "core/test.hpp"

class TestTexture2D : public Test {
  public:
    TestTexture2D(const std::string &key, const std::string &name);
    ~TestTexture2D();

    void on_update(float dt) override;
    void on_render() override;
    void on_imgui_render() override;
};
