#include <fstream>
#include <sstream>
#include <string>
#include "path.h"
#include "shader.h"

ShaderSource parse_shader(std::string filepath) {
    std::ifstream stream(project_path(filepath));

    std::string line;
    std::stringstream ss[2];
    ShaderType type = ShaderType::None;

    while (getline(stream, line)) {
        if (line.find("#type") != std::string::npos) {
            if (line.find("vertex") != std::string::npos) {
                type = ShaderType::Vertex;
            }
            if (line.find("fragment") != std::string::npos) {
                type = ShaderType::Fragment;
            }
        } else {
            ss[(int)type] << line << "\n";
        }
    }

    return {ss[0].str(), ss[1].str()};
}
