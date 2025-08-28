// 5. Write a program in C++ to create a clock class and create the following functions: 
// a. Initialize the members b. Display time c. To convert hours and minutes into minutes

#include <iostream>
using namespace std;

class Clock {
public:
    int hours, minutes;

    void initialize(int h, int m) {
        hours = h;
        minutes = m;
    }

    void displayTime() {
        cout << "Time = " << hours << " hours " << minutes << " minutes" << endl;
    }

    void convertToMinutes() {
        int totalMinutes = (hours * 60) + minutes;
        cout << "Total minutes = " << totalMinutes << endl;
    }
};

int main() {
    Clock c;
    int h, m;
    cout << "Enter hours and minutes: ";
    cin >> h >> m;

    c.initialize(h, m);
    c.displayTime();
    c.convertToMinutes();

    return 0;
}
