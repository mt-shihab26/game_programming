#include <cstdio>

#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include "window.h"

int main() {
    const int width = 1280;
    const int height = 780;

    GLFWwindow *window;

    if (!glfwInit()) {
        return 1;
    }

    glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);

    window = glfwCreateWindow(width, height, "Hello World", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return 1;
    }

    glfwMakeContextCurrent(window);

    wait_for_window_size(window, width, height);

    if (glewInit() != GLEW_OK) {
        glfwTerminate();
        return 1;
    }

    printf("Vendor:   %s\n", glGetString(GL_VENDOR));
    printf("Renderer: %s\n", glGetString(GL_RENDERER));
    printf("OpenGL:   %s\n", glGetString(GL_VERSION));
    printf("GLSL:     %s\n", glGetString(GL_SHADING_LANGUAGE_VERSION));
    printf("GLEW:     %s\n", glewGetString(GLEW_VERSION));
    printf("GLFW:     %s\n", glfwGetVersionString());

    while (!glfwWindowShouldClose(window)) {
        glClear(GL_COLOR_BUFFER_BIT);

        glBegin(GL_TRIANGLES);

        glVertex2f(-0.5f, -0.5f);
        glVertex2f(0.0f, 0.5f);
        glVertex2f(0.5f, -0.5f);

        glEnd();

        glfwSwapBuffers(window);

        glfwPollEvents();
    }

    glfwTerminate();

    return 0;
}
