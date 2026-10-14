#pragma once

#include "window.hpp"

class ImGuiLayer {
  public:
    explicit ImGuiLayer(const Window &window);
    ~ImGuiLayer();

    ImGuiLayer(const ImGuiLayer &) = delete;
    ImGuiLayer &operator=(const ImGuiLayer &) = delete;

    void begin_frame() const;
    void end_frame() const;
};
