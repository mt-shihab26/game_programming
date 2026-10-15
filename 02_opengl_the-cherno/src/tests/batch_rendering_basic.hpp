#pragma once

#include "core/test.hpp"

class BatchRenderingBasic : public Test {
    BatchRenderingBasic(const std::string &key, const std::string &name, OrthographicCamera *camera);
    ~BatchRenderingBasic();

    void on_update(float dt) override;
    void on_render() override;
    void on_imgui_render() override;
};
