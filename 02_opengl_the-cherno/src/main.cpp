#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include <cstdlib>

#include "shader.hpp"
#include "window.hpp"
#include "error.hpp"

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

    unsigned int vao;
    GL_CALL(glGenVertexArrays(1, &vao));
    GL_CALL(glBindVertexArray(vao));

    // Vertex buffer
    unsigned int buffer;
    GL_CALL(glGenBuffers(1, &buffer));
    GL_CALL(glBindBuffer(GL_ARRAY_BUFFER, buffer));
    GL_CALL(glBufferData(GL_ARRAY_BUFFER, 4 * 2 * sizeof(float), positions, GL_STATIC_DRAW));

    // Vertex attributes and layouts
    GL_CALL(glEnableVertexAttribArray(0));
    GL_CALL(glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, sizeof(float) * 2, 0));

    // Index buffer object
    unsigned int ibo;
    GL_CALL(glGenBuffers(1, &ibo));
    GL_CALL(glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibo));
    GL_CALL(glBufferData(GL_ELEMENT_ARRAY_BUFFER, 6 * sizeof(unsigned int), indices, GL_STATIC_DRAW));

    unsigned int shader = create_shader("assets/shaders/basic.glsl");

    GL_CALL(glUseProgram(shader));

    GL_CALL(int location = glGetUniformLocation(shader, "u_color"));

    ASSERT(location != -1);

    GL_CALL(glUniform4f(location, 0.8f, 0.3f, 0.8f, 1.0f));

    // reset
    GL_CALL(glBindBuffer(GL_ARRAY_BUFFER, 0));
    GL_CALL(glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0));
    GL_CALL(glUseProgram(0));

    // states
    float r = 0.0f;
    float increment = 0.05f;

    while (!glfwWindowShouldClose(window)) {
        GL_CALL(glClear(GL_COLOR_BUFFER_BIT));

        GL_CALL(glBindBuffer(GL_ARRAY_BUFFER, buffer));
        GL_CALL(glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, sizeof(float) * 2, 0));
        GL_CALL(glEnableVertexAttribArray(0));

        GL_CALL(glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ibo));

        GL_CALL(glUseProgram(shader));

        GL_CALL(glUniform4f(location, r, 0.3f, 0.8f, 1.0f));

        GL_CALL(glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, nullptr););

        if (r > 1.0f) {
            increment = -0.05f;
        } else if (r < 0.0f) {
            increment = 0.05f;
        }

        r += increment;

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    GL_CALL(glDeleteProgram(shader));

    glfwTerminate();

    return 0;
}
