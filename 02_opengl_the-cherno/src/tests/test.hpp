#pragma once

#include <functional>
#include <string>
#include <vector>

namespace test {

class Test {
  public:
    Test() {}
    virtual ~Test() {}

    virtual void on_update(float dt) {}
    virtual void on_render() {}
    virtual void on_imgui_render() {}
};

class Menu : public Test {
  public:
    Menu(Test *&current_test);
    ~Menu();

    void on_imgui_render() override;

  private:
    std::vector<std::pair<std::string, std::function<Test *()>>> m_tests;
    Test *&m_current_test;
};

} // namespace test
