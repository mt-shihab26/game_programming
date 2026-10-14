#include <imgui/imgui.h>

#include "test_menu.hpp"

TestMenu::TestMenu(Test *&current_test) : m_current_test(current_test) {
}

TestMenu::~TestMenu() {
}

void TestMenu::on_imgui_render() {
    // the menu fills the whole screen, tests get a normal floating window
    ImGui::SetNextWindowPos(ImVec2(0, 0));
    ImGui::SetNextWindowSize(ImGui::GetIO().DisplaySize);
    ImGui::Begin("Menu", nullptr, ImGuiWindowFlags_NoDecoration | ImGuiWindowFlags_NoMove);

    if (!m_tests.empty()) {
        draw_test_buttons();
    }

    ImGui::End();
}

void TestMenu::draw_test_buttons() {
    const ImGuiStyle &style = ImGui::GetStyle();
    ImVec2 available = ImGui::GetContentRegionAvail();

    // centre the column of buttons vertically in the window
    float button_height = ImGui::GetFrameHeight();
    float total_height = m_tests.size() * button_height + (m_tests.size() - 1) * style.ItemSpacing.y;
    ImGui::SetCursorPosY(ImGui::GetCursorPosY() + (available.y - total_height) / 2.0f);

    for (auto &test : m_tests) {
        // centre each button horizontally
        float button_width = ImGui::CalcTextSize(test.first.c_str()).x + style.FramePadding.x * 2.0f;
        ImGui::SetCursorPosX(ImGui::GetCursorPosX() + (available.x - button_width) / 2.0f);

        if (ImGui::Button(test.first.c_str())) {
            m_current_test = test.second();
            m_current_test->set_name(test.first);
        }
    }
}
