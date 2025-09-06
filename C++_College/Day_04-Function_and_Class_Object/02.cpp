// 2. Write a program to find factorial number using function (with parameters and without return type)

#include <iostream>
using namespace std;

void factorial(int n) {
    long long fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    cout << "Factorial of " << n << " = " << fact << endl;
}

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    factorial(num);
    return 0;
}
