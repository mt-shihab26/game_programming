#pragma once

#include <functional>
#include <string>
#include <vector>

#include "core/argv.hpp"
#include "core/log.hpp"
#include "opengl/orthographic_camera.hpp"
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
        log_info("Registering test '{}' (key: {})", name, key);

        m_entries.push_back({key, name, [this, key, name]() { return new T(key, name, &m_camera); }});
    }

    void on_update(float dt);
    void on_render();
    void on_imgui_render();

    void set_current_test(const Entry &entry);

    void open_from_args(Argv &argv);

  private:
    std::vector<Entry> m_entries;

    OrthographicCamera m_camera;

    Test *m_current_test = nullptr;

    void draw_menu();
};
