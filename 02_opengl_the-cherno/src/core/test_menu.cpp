#include <imgui/imgui.h>

#include "test_menu.hpp"

TestMenu::~TestMenu() {
    delete m_current_test;
}

void TestMenu::on_update(float dt) {
    if (m_current_test) {
        m_current_test->on_update(dt);
    }
}

void TestMenu::on_render() {
    if (m_current_test) {
        m_current_test->on_render();
    }
}

void TestMenu::on_imgui_render() {
    if (m_current_test) {
        draw_current_test();
    } else {
        draw_menu();
    }
}

void TestMenu::draw_menu() {
    // the menu fills the whole screen
    ImGui::SetNextWindowPos(ImVec2(0, 0));
    ImGui::SetNextWindowSize(ImGui::GetIO().DisplaySize);
    ImGui::Begin("Menu", nullptr, ImGuiWindowFlags_NoDecoration | ImGuiWindowFlags_NoMove);

    if (!m_tests.empty()) {
        const ImGuiStyle &style = ImGui::GetStyle();
        ImVec2 available = ImGui::GetContentRegionAvail();

        // centre the column of buttons vertically in the window
        float button_height = ImGui::GetFrameHeight();
        float total_height = m_tests.size() * button_height + (m_tests.size() - 1) * style.ItemSpacing.y;
        ImGui::SetCursorPosY(ImGui::GetCursorPosY() + (available.y - total_height) / 2.0f);

        for (const Entry &test : m_tests) {
            // centre each button horizontally
            float button_width = ImGui::CalcTextSize(test.name.c_str()).x + style.FramePadding.x * 2.0f;
            ImGui::SetCursorPosX(ImGui::GetCursorPosX() + (available.x - button_width) / 2.0f);

            if (ImGui::Button(test.name.c_str())) {
                m_current_test = test.create();
                m_current_name = test.name;
            }
        }
    }

    ImGui::End();
}

void TestMenu::draw_current_test() {
    ImGui::Begin(m_current_name.c_str());
    bool go_back = ImGui::Button("<-");
    m_current_test->on_imgui_render();
    ImGui::End();

    // close after End(), so the test isn't deleted while its window is still being drawn
    if (go_back) {
        delete m_current_test;
        m_current_test = nullptr;
    }
}
