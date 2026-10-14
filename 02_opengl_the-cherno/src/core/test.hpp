#pragma once

class Test {
  public:
    virtual ~Test() {}

    virtual void on_update(float dt) {}
    virtual void on_render() {}
    virtual void on_imgui_render() {}
};
