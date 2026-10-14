#pragma once

#include <format>
#include <iostream>
#include <string>
#include <utility>

// Logging with std::format style messages:
//
//   log_info("Registering test '{}' (key: {})", name, key);
//   log_warn("Uniform '{}' doesn't exist", name);
//   log_error("Failed to open shader '{}'", path);
//
// Info goes to stdout, warnings and errors to stderr. Each line is flushed right away,
// so nothing is lost if the program crashes.

inline void log_write(std::ostream &stream, const char *color, const char *level, const std::string &message) {
    // colour only the level tag, then reset back to the terminal's default colour
    stream << color << "[" << level << "]\033[0m " << message << std::endl;
}

template <typename... Args>
void log_info(std::format_string<Args...> format, Args &&...args) {
    log_write(std::cout, "\033[32m", "INFO", std::format(format, std::forward<Args>(args)...));
}

template <typename... Args>
void log_warn(std::format_string<Args...> format, Args &&...args) {
    log_write(std::cerr, "\033[33m", "WARN", std::format(format, std::forward<Args>(args)...));
}

template <typename... Args>
void log_error(std::format_string<Args...> format, Args &&...args) {
    log_write(std::cerr, "\033[31m", "ERROR", std::format(format, std::forward<Args>(args)...));
}
