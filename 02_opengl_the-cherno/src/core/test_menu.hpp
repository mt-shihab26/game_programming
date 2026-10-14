#pragma once

#include <functional>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

#include "test.hpp"

// Shows a full-screen list of the registered tests. Clicking one opens it in a floating window with a "<-" button.
class TestMenu {
  public:
    template <typename T>
    void register_test(const std::string &name) {
        std::cout << "Registering Test '" << name << "'\n";
        m_tests.push_back({name, []() { return std::make_unique<T>(); }});
    }

    void on_update(float dt);
    void on_render();
    void on_imgui_render();

  private:
    struct Entry {
        std::string name;
        std::function<std::unique_ptr<Test>()> create;
    };

    std::vector<Entry> m_tests;

    // nullptr while the menu is showing
    std::unique_ptr<Test> m_current_test;
    std::string m_current_name;

    void draw_menu();
    void draw_current_test();
};
