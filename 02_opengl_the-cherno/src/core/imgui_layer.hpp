#pragma once

#include "window.hpp"

class ImGuiLayer {
  public:
    explicit ImGuiLayer(const Window &window);
    ~ImGuiLayer();

    void begin_frame() const;
    void end_frame() const;
};
