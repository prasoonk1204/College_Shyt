// 3. Write a program in C++ to built a calculator using object and class concept.

#include <iostream>
using namespace std;

class Calculator {
public:
    int a, b;

    void input() {
        cout << "Enter two numbers: ";
        cin >> a >> b;
    }

    void add() {
        cout << "Sum = " << (a + b) << endl;
    }

    void subtract() {
        cout << "Subtraction = " << (a - b) << endl;
    }

    void multiply() {
        cout << "Multiplication = " << (a * b) << endl;
    }

    void divide() {
        if (b != 0)
            cout << "Division = " << (a / b) << endl;
        else
            cout << "Division not possible (b=0)" << endl;
    }
};

int main() {
    Calculator c;
    c.input();
    c.add();
    c.subtract();
    c.multiply();
    c.divide();
    return 0;
}
