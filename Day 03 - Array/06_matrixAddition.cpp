// 6. Matrix Addition (2D Array)

#include <iostream>
using namespace std;

int main() {
    int rows, cols;
    cout << "Enter number of rows and columns: ";
    cin >> rows >> cols;

    int A[100][100], B[100][100], Sum[100][100];

    cout << "Enter elements of first matrix:\n";
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            cin >> A[i][j];
        }
    }

    cout << "Enter elements of second matrix:\n";
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            cin >> B[i][j];
        }
    }

    // Matrix Addition
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            Sum[i][j] = A[i][j] + B[i][j];
        }
    }

    cout << "Sum of the matrices is:\n";
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            cout << Sum[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}

// Output

// Enter number of rows and columns: 3 3
// Enter elements of first matrix:
// 1 2 3 4 5 6 7 8 9
// Enter elements of second matrix:
// 9 8 7 6 5 4 3 2 1
// Sum of the matrices is:
// 10 10 10 
// 10 10 10 
// 10 10 10 