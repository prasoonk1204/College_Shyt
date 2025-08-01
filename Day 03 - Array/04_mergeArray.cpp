// 4. Merge Two Arrays

#include <iostream>
using namespace std;

int main() {
    int n1, n2;
    cout << "Enter the number of elements for both the arrays: ";
    cin >> n1 >> n2;
    
    int arr1[n1];
    int arr2[n2];
    
    cout << "Enter elements for array 1: ";
    
    for(int i=0; i<n1; i++){
        cin >> arr1[i];
    }
    cout << "Enter elements for array 2: ";
    
    for(int i=0; i<n2; i++){
        cin >> arr2[i];
    }
    
    int merged[n1 + n2];

    // Copy first array
    for (int i = 0; i < n1; i++) {
        merged[i] = arr1[i];
    }

    // Copy second array
    for (int i = 0; i < n2; i++) {
        merged[n1 + i] = arr2[i];
    }

    // Print merged array
    cout << "Merged Array: ";
    for (int i = 0; i < n1 + n2; i++) {
        cout << merged[i] << " ";
    }
    return 0;
}

// Output

// Enter the number of elements for both the arrays: 5 5
// Enter elements for array 1: 1 5 3 6 7
// Enter elements for array 2: 2 4 8 9 0
// Merged Array: 1 5 3 6 7 2 4 8 9 0 