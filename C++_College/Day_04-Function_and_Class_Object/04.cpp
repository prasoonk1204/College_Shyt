// 4. Write a program in C++ to find the area of rectangle using class and object concept.

#include <iostream>
using namespace std;

class Rectangle {
public:
    int length, width;

    void input() {
        cout << "Enter length and width: ";
        cin >> length >> width;
    }

    void area() {
        cout << "Area of rectangle = " << (length * width) << endl;
    }
};

int main() {
    Rectangle r;
    r.input();
    r.area();
    return 0;
}
