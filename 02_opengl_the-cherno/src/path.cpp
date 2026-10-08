#include <filesystem>
#include <string>

#include "path.hpp"

std::string project_dir() {
#if defined(DEBUG) || !defined(__linux__)
    // this file lives in <project>/src
    return std::filesystem::path(__FILE__).parent_path().parent_path().string();
#else
    // release: assets are copied next to the executable
    return std::filesystem::canonical("/proc/self/exe").parent_path().string();
#endif
}

std::string project_path(std::string relative_path) {
    return (std::filesystem::path(project_dir()) / relative_path).string();
}
