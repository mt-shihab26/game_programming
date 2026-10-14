#include <exception>
#include <iostream>

#include "core/app.hpp"

int main() {
    try {
        App app;
        app.run();
    } catch (const std::exception &error) {
        std::cerr << "error: " << error.what() << std::endl;
        return 1;
    }

    return 0;
}
