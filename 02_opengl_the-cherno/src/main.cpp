#include <cstdlib>

#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include "helper.hpp"
#include "shader.hpp"
#include "window.hpp"
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
            -0.5f, -0.5f, // 0
             0.5f, -0.5f, // 1
             0.5f,  0.5f, // 2
            -0.5f,  0.5f, // 3
        };

        unsigned int indices[] = {
            0, 1, 2,
            2, 3, 0
        };

        // clang-format on

        VertexArray va;

        VertexBuffer vb(positions, 4 * 2 * sizeof(float));

        VertexBufferLayout layout;
        layout.push<float>(2);
        va.add_buffer(vb, layout);

        IndexBuffer ib(indices, 6);

        Shader shader("assets/shaders/basic.glsl");
        shader.bind();
        shader.set_uniform_4f("u_color", 0.8f, 0.3f, 0.8f, 1.0f);

        va.unbind();
        shader.unbind();
        vb.unbind();
        ib.unbind();

        Renderer renderer;

        float r = 0.0f;
        float increment = 0.05f;

        while (!glfwWindowShouldClose(window)) {
            GL_CALL(glClear(GL_COLOR_BUFFER_BIT));

            shader.bind();
            shader.set_uniform_4f("u_color", r, 0.3f, 0.8f, 1.0f);

            renderer.draw(va, ib, shader);

            if (r > 1.0f) {
                increment = -0.05f;
            } else if (r < 0.0f) {
                increment = 0.05f;
            }

            r += increment;

            glfwSwapBuffers(window);
            glfwPollEvents();
        }
    }
    glfwTerminate();

    return 0;
}
