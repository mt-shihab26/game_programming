#include <cstdlib>

#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include "glm/ext/matrix_clip_space.hpp"

#include "supports/helper.hpp"
#include "supports/window.hpp"

#include "shader.hpp"
#include "texture.hpp"
#include "renderer.hpp"
#include "vertex_buffer.hpp"
#include "index_buffer.hpp"
#include "vertex_array.hpp"
#include "vertex_buffer_layout.hpp"

int main() {
    const int width = 1280;
    const int height = 780;

    GLFWwindow *window;

    // Mesa returns the newest version it has, so pin it to 3.3
    setenv("MESA_GL_VERSION_OVERRIDE", "3.3", 1);
    setenv("MESA_GLSL_VERSION_OVERRIDE", "330", 1);

    if (!glfwInit()) {
        return 1;
    }

    glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    window = glfwCreateWindow(width, height, "Hello World", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return 1;
    }

    glfwMakeContextCurrent(window);

    wait_for_window_size(window, width, height);

    glfwSwapInterval(1);

    if (glewInit() != GLEW_OK) {
        glfwTerminate();
        return 1;
    }

    print_libaray_versions();

    {
        // clang-format off

        float positions[] = {
            100.0f, 100.0f, 0.0f, 0.0f, // 0
            200.0f, 100.0f, 1.0f, 0.0f, // 1
            200.0f, 200.5f, 1.0f, 1.0f, // 2
            100.0f, 200.5f, 0.0f, 1.0f  // 3
        };

        unsigned int indices[] = {
            0, 1, 2,
            2, 3, 0
        };

        // clang-format on

        GL_CALL(glEnable(GL_BLEND));
        GL_CALL(glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA));

        VertexArray va;

        VertexBuffer vb(positions, 4 * 4 * sizeof(float));

        VertexBufferLayout layout;
        layout.push<float>(2);
        layout.push<float>(2);
        va.add_buffer(vb, layout);

        IndexBuffer ib(indices, 6);

        glm::mat4 proj = glm::ortho(0.0f, (float)width, 0.0f, (float)height, -1.0f, 1.0f);

        Shader shader("assets/shaders/basic.glsl");
        shader.bind();
        shader.set_uniform_1i("u_texture", 0);
        shader.set_uniform_mat4f("u_mvp", proj);

        Texture texture("assets/textures/omarchy-logo-tokyo-night.png");
        texture.bind();

        va.unbind();
        shader.unbind();
        vb.unbind();
        ib.unbind();

        Renderer renderer;

        while (!glfwWindowShouldClose(window)) {
            renderer.clear();
            shader.bind();
            renderer.draw(va, ib, shader);

            glfwSwapBuffers(window);
            glfwPollEvents();
        }
    }
    glfwTerminate();

    return 0;
}
