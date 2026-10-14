#include <imgui/imgui.h>
#include <imgui/imgui_impl_glfw.h>
#include <imgui/imgui_impl_opengl3.h>

#include "imgui_layer.hpp"

ImGuiLayer::ImGuiLayer(const Window &window) {
    ImGui::CreateContext();
    ImGui_ImplGlfw_InitForOpenGL(window.handle(), true);
    ImGui_ImplOpenGL3_Init("#version 330");
    ImGui::StyleColorsDark();

    ImGuiIO &io = ImGui::GetIO();
    // window positions and sizes are set in code, so don't save them to imgui.ini
    io.IniFilename = nullptr;
    // the default pixel font looks jagged at fractional scales (1.25), the vector one stays crisp
    io.Fonts->AddFontDefaultVector();

    // scale text and widgets by the monitor scale, otherwise the 13px font is only ~16 real pixels tall
    float content_scale = window.content_scale();
    ImGuiStyle &style = ImGui::GetStyle();
    style.ScaleAllSizes(content_scale);
    style.FontScaleDpi = content_scale;
}

ImGuiLayer::~ImGuiLayer() {
    ImGui_ImplOpenGL3_Shutdown();
    ImGui_ImplGlfw_Shutdown();
    ImGui::DestroyContext();
}

void ImGuiLayer::begin_frame() const {
    ImGui_ImplOpenGL3_NewFrame();
    ImGui_ImplGlfw_NewFrame();
    ImGui::NewFrame();
}

void ImGuiLayer::end_frame() const {
    ImGui::Render();
    ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());
}
