// Write a program in C++ to show the use of friend function in two classes.
#include <iostream>
using namespace std;

class ClassB;

class ClassA {
private:
    int valueA;
public:
    ClassA(int a) : valueA(a) {}
    friend void add(ClassA, ClassB);
};

class ClassB {
private:
    int valueB;
public:
    ClassB(int b) : valueB(b) {}
    friend void add(ClassA, ClassB);
};

void add(ClassA objA, ClassB objB) {
    cout << "Sum of values from ClassA and ClassB: " << (objA.valueA + objB.valueB) << endl;
}

int main() {
    ClassA a(10);
    ClassB b(20);
    add(a, b);
    return 0;
}
