// 1. Write a program to do sum and subtraction of two numbers using function (without parameters and
// without return type)

#include <iostream>
using namespace std;

void sumAndSubtraction() {
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;

    cout << "Sum = " << (a + b) << endl;
    cout << "Subtraction = " << (a - b) << endl;
}

int main() {
    sumAndSubtraction(); // function call
    return 0;
}
