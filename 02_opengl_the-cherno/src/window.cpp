#include <cstdio>

#include <GL/glew.h>
#include <GLFW/glfw3.h>

#include "window.h"

// Works around two problems when opening a window on Hyprland (Wayland):
//
// 1. Wrong window size: Hyprland first sizes the new window as a tile and only
//    then floats it, and GLFW keeps that tile size instead of the size passed
//    to glfwCreateWindow. Asking for the size again fixes it.
//
// 2. Off-centre drawing: OpenGL sets the viewport once, when the context is
//    made current. On a scaled display (e.g. 1.25) the framebuffer only grows
//    to its real pixel size a few frames later, so the viewport ends up smaller
//    than the framebuffer and everything is drawn in the bottom-left corner.
//    Drawing a few empty frames until the framebuffer changes, then setting the
//    viewport to match it, fixes it.
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

void print_libaray_versions() {
    printf("Vendor:   %s\n", glGetString(GL_VENDOR));
    printf("Renderer: %s\n", glGetString(GL_RENDERER));
    printf("OpenGL:   %s\n", glGetString(GL_VERSION));
    printf("GLSL:     %s\n", glGetString(GL_SHADING_LANGUAGE_VERSION));
    printf("GLEW:     %s\n", glewGetString(GLEW_VERSION));
    printf("GLFW:     %s\n", glfwGetVersionString());
}
