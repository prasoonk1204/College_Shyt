// Write a program in C++ to calculate the sum of natural numbers upto n terms using a constructor.

#include <iostream>
using namespace std;

class SumNatural {
    int n, sum;

public:
    // Constructor to calculate sum
    SumNatural(int num) {
        n = num;
        sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        cout << "Sum of first " << n << " natural numbers = " << sum << endl;
    }
};

int main() {
    int n;
    cout << "Enter the number of terms: ";
    cin >> n;

    // Creating object and passing n to constructor
    SumNatural s(n);

    return 0;
}
