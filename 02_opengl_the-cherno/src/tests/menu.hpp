#pragma once

#include <functional>
#include <iostream>
#include <string>

#include "test.hpp"

namespace test {

class Menu : public Test {
  public:
    Menu(Test *&current_test);
    ~Menu();

    void on_imgui_render() override;

    template <typename T>
    void register_test(const std::string &name) {
        std::cout << "Registering Test '" << name << "'\n";
        m_tests.push_back(std::make_pair(name, []() { return new T(); }));
    }

    const std::string &get_current_test_name() const { return m_current_test->get_name(); }

  private:
    std::vector<std::pair<std::string, std::function<Test *()>>> m_tests;
    Test *&m_current_test;

    void draw_test_buttons();
};
} // namespace test
