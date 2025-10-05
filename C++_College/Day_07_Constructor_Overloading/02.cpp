// Write a program in C++ to find simple interest using constructor overloading.

#include <iostream>
using namespace std;

class SimpleInterest {
    float principal, rate, time, si;

public:
    // Constructor 1 - Default values
    SimpleInterest() {
        principal = 1000;
        rate = 5;
        time = 2;
        si = (principal * rate * time) / 100;
        cout << "Simple Interest (default values): " << si << endl;
    }

    // Constructor 2 - When values are given by user
    SimpleInterest(float p, float r, float t) {
        principal = p;
        rate = r;
        time = t;
        si = (principal * rate * time) / 100;
        cout << "Simple Interest (user values): " << si << endl;
    }
};

int main() {
    // Using default constructor
    SimpleInterest s1;

    // Using parameterized constructor
    float p, r, t;
    cout << "\nEnter Principal, Rate and Time: ";
    cin >> p >> r >> t;

    SimpleInterest s2(p, r, t);

    return 0;
}
