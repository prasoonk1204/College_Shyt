// Write a program in C++ where derived class is inherited using protected keyword.

#include <iostream>
using namespace std;

class Animal {
public:
    void eat() {
        cout << "This animal eats food." << endl;
    }
};

class Dog : protected Animal {
public:
    void bark() {
        cout << "The dog barks." << endl;
    }

    void callEat() {
        eat();
    }
};

class Puppy : public Dog {
public:
    void play() {
        cout << "The puppy plays." << endl;
        eat();
    }
};

int main() {
    Dog d;
    Puppy p;

    // d.eat();   // Error: eat() is protected in Dog
    d.bark();
    d.callEat();

    // p.eat();   // Error: still protected
    p.play();

    return 0;
}