#include <filesystem>
#include <string>
#include "path.h"

std::string project_dir() {
    // this file lives in <project>/src
    return std::filesystem::path(__FILE__).parent_path().parent_path().string();
}

std::string project_path(std::string relative_path) {
    return (std::filesystem::path(project_dir()) / relative_path).string();
}
