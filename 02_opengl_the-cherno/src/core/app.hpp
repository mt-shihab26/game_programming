#pragma once

#include "imgui_layer.hpp"
#include "opengl/renderer.hpp"
#include "test_runner.hpp"
#include "window.hpp"

class App {
  public:
    App();

    void run();

  private:
    Window m_window;
    ImGuiLayer m_imgui_layer;
    Renderer m_renderer;
    test::TestRunner m_test_runner;
};
