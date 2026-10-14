#pragma once

#include <functional>
#include <iostream>
#include <string>
#include <vector>

#include "test.hpp"

class TestMenu {
  public:
    ~TestMenu();

    template <typename T>
    void register_test(const std::string &name) {
        std::cout << "Registering Test '" << name << "'\n";
        m_tests.push_back({name, []() { return new T(); }});
    }

    void on_update(float dt);
    void on_render();
    void on_imgui_render();

  private:
    struct Entry {
        std::string name;
        std::function<Test *()> create;
    };

    std::vector<Entry> m_tests;

    Test *m_current_test = nullptr;
    std::string m_current_name;

    void draw_menu();
    void draw_current_test();
};
