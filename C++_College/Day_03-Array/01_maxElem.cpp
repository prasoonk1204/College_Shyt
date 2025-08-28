// 1. Find the Maximum Element in an Array

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    
    int arr[n];
    cout << "Enter elements: ";
    
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    
    int max=arr[0];
    for (int j=1; j<n; j++){
        if(max<arr[j]){
            max=arr[j];
        }
    }
    
    cout << max << " is the largest number.";
    
    return 0;
}

// Output

// Enter the number of elements: 5
// Enter elements: 10 39 33 56 45
// 56 is the largest number.