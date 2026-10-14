#include <imgui/imgui.h>

#include "test_menu.hpp"

TestMenu::TestMenu() {
}

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

void TestMenu::set_current_test(const Entry &entry) {
    m_current_key = entry.key;
    m_current_test = entry.create();
    m_current_name = entry.name;
}

void TestMenu::open_from_args(Argv &argv) {
}

void TestMenu::draw_menu() {
    ImGui::SetNextWindowPos(ImVec2(0, 0));
    ImGui::SetNextWindowSize(ImGui::GetIO().DisplaySize);
    ImGui::Begin("Menu", nullptr, ImGuiWindowFlags_NoDecoration | ImGuiWindowFlags_NoMove);

    if (!m_tests.empty()) {
        const ImGuiStyle &style = ImGui::GetStyle();
        ImVec2 available = ImGui::GetContentRegionAvail();

        float button_height = ImGui::GetFrameHeight();
        float total_height = m_tests.size() * button_height + (m_tests.size() - 1) * style.ItemSpacing.y;
        ImGui::SetCursorPosY(ImGui::GetCursorPosY() + (available.y - total_height) / 2.0f);

        int number = 1;
        for (const Entry &test : m_tests) {
            std::string label = std::to_string(number) + ". " + test.name + " (" + test.key + ")";
            number++;

            float button_width = ImGui::CalcTextSize(label.c_str()).x + style.FramePadding.x * 2.0f;
            ImGui::SetCursorPosX(ImGui::GetCursorPosX() + (available.x - button_width) / 2.0f);
            if (ImGui::Button(label.c_str())) {
                set_current_test(test);
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
