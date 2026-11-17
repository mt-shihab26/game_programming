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
        std::shared_ptr<Entity> e0;
        {
            std::shared_ptr<Entity> entity = std::make_shared<Entity>();
            std::shared_ptr<Entity> e2 = entity;
            e0 = entity;

            entity->print();
            e2->print();
        }
        e0->print();
    }

    return 0;
}
