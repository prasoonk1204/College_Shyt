// 1. Write a program in C++ to calculate the area of rectangle , circle and triangle using method overloading.

#include <iostream>
using namespace std;

class Area {
public:
    // Rectangle (length, breadth)
    float calculate(float length, float breadth) {
        return length * breadth;
    }

    // Circle (radius)
    float calculate(float radius) {
        return 3.14159 * radius * radius;
    }

    // Triangle (base, height)
    float calculate(double base, double height) {
        return 0.5 * base * height;
    }
};

int main() {
    Area a;

    float length, breadth, radius;
    double base, height;

    cout << "Enter length and breadth of rectangle: ";
    cin >> length >> breadth;
    cout << "Area of rectangle = " << a.calculate(length, breadth) << endl;

    cout << "Enter radius of circle: ";
    cin >> radius;
    cout << "Area of circle = " << a.calculate(radius) << endl;

    cout << "Enter base and height of triangle: ";
    cin >> base >> height;
    cout << "Area of triangle = " << a.calculate(base, height) << endl;

    return 0;
}
