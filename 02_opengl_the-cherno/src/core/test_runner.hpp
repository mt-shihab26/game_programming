#pragma once

#include <string>

#include "tests/test.hpp"

namespace test {

// Owns the menu and whichever test is open, and draws the one that is active.
class TestRunner {
  public:
    TestRunner();
    ~TestRunner();

    TestRunner(const TestRunner &) = delete;
    TestRunner &operator=(const TestRunner &) = delete;

    template <typename T>
    void register_test(const std::string &name) {
        m_menu->register_test<T>(name);
    }

    void on_update(float dt);
    void on_render();
    void on_imgui_render();

    Menu *get_menu() { return m_menu; }

  private:
    Test *m_current_test;
    Menu *m_menu;

    void close_current_test();
};

} // namespace test
