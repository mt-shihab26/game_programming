#include <imgui/imgui.h>

#include "test_runner.hpp"

TestRunner::TestRunner() : m_current_test(nullptr), m_menu(nullptr) {
    m_menu = new TestMenu(m_current_test);
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
        m_menu->on_imgui_render();
        return;
    }

    ImGui::Begin(get_menu()->get_current_test_name().c_str());
    bool go_back = ImGui::Button("<-");
    m_current_test->on_imgui_render();
    ImGui::End();

    // close after End(), so the test isn't deleted while its window is still being drawn
    if (go_back) {
        close_current_test();
    }
}

void TestRunner::close_current_test() {
    if (m_current_test != m_menu) {
        delete m_current_test;
        m_current_test = m_menu;
    }
}
