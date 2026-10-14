#include <cstdio>
#include <cstdlib>
#include <stdexcept>

#include <glew/GL/glew.h>
#include <glfw/GLFW/glfw3.h>

#include "opengl/helper.hpp"

#include "window.hpp"

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
static void wait_for_window_size(GLFWwindow *window, int width, int height) {
    // Hyprland sizes the window as a tile before floating it, so ask for the size again
    glfwSetWindowSize(window, width, height);

    int initialWidth, initialHeight;
    glfwGetFramebufferSize(window, &initialWidth, &initialHeight);

    int framebufferWidth = initialWidth;
    int framebufferHeight = initialHeight;

    // Tiling WMs (Hyprland) resize the framebuffer only after the first frames are drawn
    for (int i = 0; i < 10; i++) {
        GL_CALL(glClear(GL_COLOR_BUFFER_BIT));
        glfwSwapBuffers(window);
        glfwPollEvents();

        glfwGetFramebufferSize(window, &framebufferWidth, &framebufferHeight);
        if (framebufferWidth != initialWidth || framebufferHeight != initialHeight) {
            break;
        }
    }

    GL_CALL(glViewport(0, 0, framebufferWidth, framebufferHeight));
}

static void print_libaray_versions() {
    GL_CALL(printf("Vendor:   %s\n", glGetString(GL_VENDOR)));
    GL_CALL(printf("Renderer: %s\n", glGetString(GL_RENDERER)));
    GL_CALL(printf("OpenGL:   %s\n", glGetString(GL_VERSION)));
    GL_CALL(printf("GLSL:     %s\n", glGetString(GL_SHADING_LANGUAGE_VERSION)));
    printf("GLEW:     %s\n", glewGetString(GLEW_VERSION));
    printf("GLFW:     %s\n", glfwGetVersionString());
}

Window::Window(int width, int height, const std::string &title) : m_window(nullptr) {
    // Mesa returns the newest version it has, so pin it to 3.3
    setenv("MESA_GL_VERSION_OVERRIDE", "3.3", 1);
    setenv("MESA_GLSL_VERSION_OVERRIDE", "330", 1);

    if (!glfwInit()) {
        throw std::runtime_error("failed to initialise GLFW");
    }

    glfwWindowHint(GLFW_RESIZABLE, GLFW_FALSE);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    m_window = glfwCreateWindow(width, height, title.c_str(), nullptr, nullptr);
    if (!m_window) {
        glfwTerminate();
        throw std::runtime_error("failed to create the window");
    }

    glfwMakeContextCurrent(m_window);

    wait_for_window_size(m_window, width, height);

    glfwSwapInterval(1);

    if (glewInit() != GLEW_OK) {
        glfwTerminate();
        throw std::runtime_error("failed to initialise GLEW");
    }

    print_libaray_versions();
}

Window::~Window() {
    glfwTerminate();
}

bool Window::should_close() const {
    return glfwWindowShouldClose(m_window);
}

void Window::swap_buffers() const {
    glfwSwapBuffers(m_window);
}

void Window::poll_events() const {
    glfwPollEvents();
}

float Window::content_scale() const {
    // GLFW's content scale reports 1.0 on Wayland fractional scaling, so derive it from the framebuffer
    int framebuffer_width, window_width;
    glfwGetFramebufferSize(m_window, &framebuffer_width, nullptr);
    glfwGetWindowSize(m_window, &window_width, nullptr);
    return (float)framebuffer_width / (float)window_width;
}
