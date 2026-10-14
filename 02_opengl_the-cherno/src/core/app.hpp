#pragma once

#include "imgui_layer.hpp"
#include "opengl_layer.hpp"
#include "test_runner.hpp"
#include "window.hpp"

class App {
  public:
    App();
    void run();

  private:
    Window m_window;
    OpenGLLayer m_opengl_layer;
    ImGuiLayer m_imgui_layer;
    test::TestRunner m_test_runner;
};
