// Write a program in C++ where derived class is inherited using private keyword.

#include <iostream>
using namespace std;

class Animal {
public:
    void eat() {
        cout << "This animal eats food." << endl;
    }
};

class Dog : private Animal {
public:
    void bark() {
        cout << "The dog barks." << endl;
    }

    void callEat() {
        eat();
    }
};

int main() {
    Dog d;

    // d.eat();  //  Error: eat() is private in Dog
    d.bark();
    d.callEat();

    return 0;
}
