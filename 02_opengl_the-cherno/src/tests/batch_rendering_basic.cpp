#include "core/test.hpp"

#include "batch_rendering_basic.hpp"

BatchRenderingBasic::BatchRenderingBasic(const std::string &key, const std::string &name, OrthographicCamera *camera)
    : Test(key, name, camera) {
}

BatchRenderingBasic::~BatchRenderingBasic() {
}

void BatchRenderingBasic::on_update(float dt) {
}

void BatchRenderingBasic::on_render() {
}

void BatchRenderingBasic::on_imgui_render() {
}
