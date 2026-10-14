#pragma once

#include <string>
#include <vector>

class Argv {
  public:
    Argv(int i_argc, char *i_argv[]);

    bool empty();
    std::string first();

  private:
    std::vector<std::string> argv;
};
