// 2. Write a program in C++ to calculate the absolute value of a number giver by the user using method overloading.

#include <iostream>
using namespace std;

class Absolute {
public:
    int absolute(int n) {
        return (n < 0) ? -n : n;
    }

    float absolute(float n) {
        return (n < 0) ? -n : n;
    }

    double absolute(double n) {
        return (n < 0) ? -n : n;
    }
};

int main() {
    Absolute absObj;

    int i;
    float f;
    double d;

    cout << "Enter an integer: ";
    cin >> i;
    cout << "Absolute value = " << absObj.absolute(i) << endl;

    cout << "Enter a float: ";
    cin >> f;
    cout << "Absolute value = " << absObj.absolute(f) << endl;

    cout << "Enter a double: ";
    cin >> d;
    cout << "Absolute value = " << absObj.absolute(d) << endl;

    return 0;
}
