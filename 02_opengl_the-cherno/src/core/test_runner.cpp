#include <imgui/imgui.h>

#include "test_runner.hpp"

namespace test {

TestRunner::TestRunner() : m_current_test(nullptr), m_menu(nullptr) {
    // the menu switches tests by writing to m_current_test
    m_menu = new Menu(m_current_test);
    m_current_test = m_menu;
}

TestRunner::~TestRunner() {
    close_current_test();
    delete m_menu;
}

void TestRunner::on_update(float dt) {
    m_current_test->on_update(dt);
}

void TestRunner::on_render() {
    m_current_test->on_render();
}

void TestRunner::on_imgui_render() {
    if (m_current_test == m_menu) {
        // the menu fills the whole screen, tests get a normal floating window
        ImGui::SetNextWindowPos(ImVec2(0, 0));
        ImGui::SetNextWindowSize(ImGui::GetIO().DisplaySize);
        ImGui::Begin("Menu", nullptr, ImGuiWindowFlags_NoDecoration | ImGuiWindowFlags_NoMove);
    } else {
        ImGui::Begin("Test");
        if (ImGui::Button("<-")) {
            close_current_test();
        }
    }

    m_current_test->on_imgui_render();
    ImGui::End();
}

void TestRunner::close_current_test() {
    if (m_current_test != m_menu) {
        delete m_current_test;
        m_current_test = m_menu;
    }
}

} // namespace test
