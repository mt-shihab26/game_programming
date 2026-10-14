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
    // members are destroyed in reverse order: tests and ImGui go before the window and its GL context
    Window m_window;
    ImGuiLayer m_imgui;
    Renderer m_renderer;
    test::TestRunner m_tests;
};
