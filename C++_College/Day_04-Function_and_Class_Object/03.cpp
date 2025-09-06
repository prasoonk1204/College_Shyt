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
    int choice;
    
    c.input();

    cout << "Calculator Menu:\n";
    cout << "1. Addition\n";
    cout << "2. Subtraction\n";
    cout << "3. Multiplication\n";
    cout << "4. Division\n";
    cout << "Enter your choice (1-4): ";
    cin >> choice;

    switch (choice) {
        case 1:
            c.add();
            break;
        case 2:
            c.subtract();
            break;
        case 3:
            c.multiply();
            break;
        case 4:
            c.divide();
            break;
        default:
            cout << "Invalid choice!" << endl;
    }

    return 0;
}
