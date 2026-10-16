#include <exception>

#include "core/argv.hpp"
#include "core/imgui_layer.hpp"
#include "core/log.hpp"
#include "core/opengl_layer.hpp"
#include "core/test_menu.hpp"
#include "core/window.hpp"

#include "tests/batch_rendering_basic.hpp"
#include "tests/batch_rendering_color.hpp"
#include "tests/batch_rendering_dynamic_geometry.hpp"
#include "tests/batch_rendering_dynamic_indices.hpp"
#include "tests/batch_rendering_texture.hpp"
#include "tests/test_clear_color.hpp"
#include "tests/test_texture_2d.hpp"

class App {
  public:
    App(Argv &argv) : m_window(1280, 780, "OpenGL - The Cherno"), m_imgui_layer(m_window) {
        m_test_menu.register_test<TestClearColor>("clear-color", "Clear Color");
        m_test_menu.register_test<TestTexture2D>("texture-2d", "Texture 2D");
        m_test_menu.register_test<BatchRenderingBasic>("batch-rendering-basic", "Batch Rendering Basic");
        m_test_menu.register_test<BatchRenderingColor>("batch-rendering-color", "Batch Rendering Color");
        m_test_menu.register_test<BatchRenderingTexture>("batch-rendering-texture", "Batch Rendering Texture");
        m_test_menu.register_test<BatchRenderingDynamicGeometry>("batch-rendering-dynamic-geometry", "Batch Rendering Dynamic Geometry");
        m_test_menu.register_test<BatchRenderingDynamicIndices>("batch-rendering-dynamic-indices", "Batch Rendering Dynamic Indices");

        m_test_menu.open_from_args(argv);
    }

    void run() {
        while (!m_window.should_close()) {
            m_opengl_layer.begin_frame();
            m_imgui_layer.begin_frame();

            m_test_menu.on_update(0.0f);
            m_test_menu.on_render();
            m_test_menu.on_imgui_render();

            m_imgui_layer.end_frame();

            m_window.end_frame();
        }
    }

  private:
    Window m_window;
    OpenGLLayer m_opengl_layer;
    ImGuiLayer m_imgui_layer;
    TestMenu m_test_menu;
};

int main(int argc, char *argv[]) {
    try {
        Argv argv_obj(argc, argv);
        App app(argv_obj);
        app.run();
    } catch (const std::exception &error) {
        log_error("{}", error.what());
        return 1;
    }
    return 0;
}
