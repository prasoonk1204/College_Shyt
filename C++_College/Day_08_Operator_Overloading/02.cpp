// Create a class called Complex for performing following operations: 
// a.Overload increment and decrement operators for increasing and decreasing
// complex number values (Unary operator overload).
// b.Overload ‘+’ op and ’-‘op for complex numbers
// (binary operator overloading).

#include <iostream>
using namespace std;

class Complex {
    int real, img;
public:
    Complex(int r = 0, int i = 0) {
        real = r;
        img = i;
    }
    Complex operator++() {
        real++;
        img++;
        return Complex(real, img);
    }
    Complex operator--() {
        real--;
        img--;
        return Complex(real, img);
    }
    Complex operator+(Complex c) {
        Complex temp;
        temp.real = real + c.real;
        temp.img = img + c.img;
        return temp;
    }
    Complex operator-(Complex c) {
        Complex temp;
        temp.real = real - c.real;
        temp.img = img - c.img;
        return temp;
    }
    void display() {
        cout << real << " + " << img << "i" << endl;
    }
};

int main() {
    Complex c1(2, 3), c2(4, 5), c3;
    c3 = c1 + c2;
    c3.display();
    c3 = c1 - c2;
    c3.display();
    ++c1;
    c1.display();
    --c2;
    c2.display();
    return 0;
}