#pragma once

// each level also logs everything above it, except HighAssert which only logs high
enum class DebugLogLevel {
    None = 0,
    HighAssert = 1,
    High = 2,
    Medium = 3,
    Low = 4,
    Notification = 5,
};

void set_gl_debug_log_level(DebugLogLevel level);

void enable_gl_debugging();
