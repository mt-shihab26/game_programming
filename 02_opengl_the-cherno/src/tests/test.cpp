
#include "test.hpp"
#include <imgui/imgui.h>

namespace test {

Menu::Menu(Test *&current_test) : m_current_test(current_test) {
}

Menu::~Menu() {
}

void Menu::on_imgui_render() {
    for (auto &test : m_tests) {
        if (ImGui::Button(test.first.c_str())) {
            m_current_test = test.second();
        }
    }
}

} // namespace test
