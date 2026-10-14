
#include "test.hpp"
#include <imgui/imgui.h>

namespace test {

Menu::Menu(Test *&current_test) : m_current_test(current_test) {
}

Menu::~Menu() {
}

void Menu::on_imgui_render() {
    if (m_tests.empty()) {
        return;
    }

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
        }
    }
}

} // namespace test
