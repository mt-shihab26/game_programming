#include <algorithm>
#include <imgui/imgui.h>

#include "test_menu.hpp"

TestMenu::TestMenu() {
}

TestMenu::~TestMenu() {
    delete m_current_test;
}

void TestMenu::on_update(float dt) {
    if (m_current_test) {
        m_current_test->get_camera()->on_update();
        m_current_test->on_update(dt);
    }
}

void TestMenu::on_render() {
    if (m_current_test) {
        m_current_test->get_camera()->on_render();
        m_current_test->on_render();
    }
}

void TestMenu::on_imgui_render() {
    if (m_current_test) {
        bool go_back = m_current_test->get_camera()->on_imgui_render();
        draw_current_test();

        // close after both windows are drawn, so the test isn't deleted while still in use
        if (go_back) {
            delete m_current_test;
            m_current_test = nullptr;
        }
    } else {
        draw_menu();
    }
}

void TestMenu::set_current_test(const Entry &entry) {
    delete m_current_test;

    m_current_test = entry.create();
}

void TestMenu::open_from_args(Argv &argv) {
    if (argv.empty()) {
        return;
    }
    std::string first = argv.first();
    auto entry = std::find_if(m_entries.begin(), m_entries.end(), [&first](const Entry &entry) {
        return first == entry.key;
    });
    if (entry != m_entries.end()) {
        set_current_test(*entry);
    }
}

void TestMenu::draw_menu() {
    ImGui::SetNextWindowPos(ImVec2(0, 0));
    ImGui::SetNextWindowSize(ImGui::GetIO().DisplaySize);
    ImGui::Begin("Menu", nullptr, ImGuiWindowFlags_NoDecoration | ImGuiWindowFlags_NoMove);

    if (!m_entries.empty()) {
        const ImGuiStyle &style = ImGui::GetStyle();
        ImVec2 available = ImGui::GetContentRegionAvail();

        const char *title = "Tests";

        // title line + one gap below it + the buttons
        float title_height = ImGui::GetTextLineHeight() + style.ItemSpacing.y * 2.0f;
        float button_height = ImGui::GetFrameHeight();
        float total_height = title_height + m_entries.size() * button_height + (m_entries.size() - 1) * style.ItemSpacing.y;
        ImGui::SetCursorPosY(ImGui::GetCursorPosY() + (available.y - total_height) / 2.0f);

        float title_width = ImGui::CalcTextSize(title).x;
        ImGui::SetCursorPosX(ImGui::GetCursorPosX() + (available.x - title_width) / 2.0f);
        ImGui::TextUnformatted(title);
        ImGui::Dummy(ImVec2(0.0f, style.ItemSpacing.y));

        int number = 1;
        for (const Entry &test : m_entries) {
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
    // SetNextWindow* only applies to the next Begin(), so it has to be set here, before the test's window opens
    float content_scale = ImGui::GetIO().DisplayFramebufferScale.x;
    // pivot (1, 0) anchors the window by its top-right corner
    ImVec2 top_right(ImGui::GetIO().DisplaySize.x, 0.0f);
    ImGui::SetNextWindowPos(top_right, ImGuiCond_Appearing, ImVec2(1.0f, 0.0f));
    ImGui::SetNextWindowSize(ImVec2(340 * content_scale, 180 * content_scale), ImGuiCond_FirstUseEver);

    ImGui::Begin(m_current_test->get_name().c_str());
    m_current_test->on_imgui_render();
    ImGui::End();
}
