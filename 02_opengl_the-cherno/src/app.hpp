#pragma once

#include "core/imgui_layer.hpp"
#include "core/opengl_layer.hpp"
#include "core/test_menu.hpp"
#include "core/window.hpp"

class App {
  public:
    App();
    void run();

  private:
    Window m_window;
    OpenGLLayer m_opengl_layer;
    ImGuiLayer m_imgui_layer;
    TestMenu m_test_menu;
};
