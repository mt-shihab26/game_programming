#pragma once

#if defined(_MSC_VER)
#define DEBUG_BREAK() __debugbreak()
#elif defined(__clang__)
// stops in the calling function, raise() would stop inside libc instead
#define DEBUG_BREAK() __builtin_debugtrap()
#else
#include <csignal>
#define DEBUG_BREAK() raise(SIGTRAP)
#endif

#define ASSERT(x)          \
    do {                   \
        if (!(x))          \
            DEBUG_BREAK(); \
    } while (0)

#define GL_CALL(x)    \
    gl_clear_error(); \
    x;                \
    ASSERT(gl_log_call())

void gl_clear_error();

bool gl_log_call();
