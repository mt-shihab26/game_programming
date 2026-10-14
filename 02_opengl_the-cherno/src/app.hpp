#pragma once

#include "core/imgui_layer.hpp"
#include "core/opengl_layer.hpp"
#include "core/test_runner.hpp"
#include "core/window.hpp"

class App {
  public:
    App();
    void run();

  private:
    Window m_window;
    OpenGLLayer m_opengl_layer;
    ImGuiLayer m_imgui_layer;
    TestRunner m_test_runner;
};
