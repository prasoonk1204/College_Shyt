#include <iostream>
using namespace std;

void addition() {
    int a, b, sum;
    cout << "Enter two numbers for addition: ";
    cin >> a >> b;
    sum = a + b;
    cout << "Sum = " << sum << endl;
}

void subtraction() {
    int a, b, diff;
    cout << "Enter two numbers for subtraction: ";
    cin >> a >> b;
    diff = a - b;
    cout << "Difference = " << diff << endl;
}

int main() {
    cout << "=== Addition ===" << endl;
    addition();

    cout << "\n=== Subtraction ===" << endl;
    subtraction();

    return 0;
}