#include <iostream>
#include <memory>

class Entity {
public:
    Entity() {
        std::cout << "Created Entity\n";
    }

    ~Entity() {
        std::cout << "Destroyed Entity\n";
    }

    void print() {
        std::cout << "Hello Entity\n";
    }
};

int main() {
    {
        std::unique_ptr<Entity> entity = std::make_unique<Entity>();
        entity->print();
    }

    return 0;
}
