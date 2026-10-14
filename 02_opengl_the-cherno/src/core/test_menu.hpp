#pragma once

#include <functional>
#include <iostream>
#include <string>
#include <vector>

#include "core/argv.hpp"
#include "test.hpp"

struct Entry {
    std::string key;
    std::string name;
    std::function<Test *()> create;
};

class TestMenu {
  public:
    TestMenu();
    ~TestMenu();

    template <typename T>
    void register_test(const std::string &key, const std::string &name) {
        std::cout << "Registering Test '" << name << "' (key: " << key << ")\n";
        m_entries.push_back({key, name, [key, name]() { return new T(key, name); }});
    }

    void on_update(float dt);
    void on_render();
    void on_imgui_render();

    void set_current_test(const Entry &entry);

    void open_from_args(Argv &argv);

  private:
    std::vector<Entry> m_entries;

    Test *m_current_test = nullptr;

    void draw_menu();
    void draw_current_test();
};
