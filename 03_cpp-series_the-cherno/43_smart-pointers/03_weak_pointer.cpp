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
        std::weak_ptr<Entity> e1;
        {
            std::shared_ptr<Entity> entity = std::make_shared<Entity>();
            entity->print();

            std::weak_ptr<Entity> e2 = entity;

            if (std::shared_ptr<Entity> ex2 = e2.lock()) ex2->print();

            e1 = entity;
        }
        if (std::shared_ptr<Entity> ex1 = e1.lock())
            ex1->print();
        else
            std::cout << "ptr is expired\n";
    }

    return 0;
}
