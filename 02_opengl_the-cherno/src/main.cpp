#include <GLFW/glfw3.h>

void wait_for_window_size(GLFWwindow *window, int width, int height) {
    // Hyprland sizes the window as a tile before floating it, so ask for the size again
    glfwSetWindowSize(window, width, height);

    int initialWidth, initialHeight;
    glfwGetFramebufferSize(window, &initialWidth, &initialHeight);

    int framebufferWidth = initialWidth;
    int framebufferHeight = initialHeight;

    // Tiling WMs (Hyprland) resize the framebuffer only after the first frames are drawn
    for (int i = 0; i < 10; i++) {
        glClear(GL_COLOR_BUFFER_BIT);
        glfwSwapBuffers(window);
        glfwPollEvents();

        glfwGetFramebufferSize(window, &framebufferWidth, &framebufferHeight);
        if (framebufferWidth != initialWidth || framebufferHeight != initialHeight) {
            break;
        }
    }

    glViewport(0, 0, framebufferWidth, framebufferHeight);
}

int main() {
    const int width = 1280;
    const int height = 780;

    GLFWwindow *window;

    if (!glfwInit()) {
        return -1;
    }

    glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);

    window = glfwCreateWindow(width, height, "Hello World", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);

    wait_for_window_size(window, width, height);

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
