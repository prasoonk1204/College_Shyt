// 2. Sort an Array in Ascending Order (Bubble Sort)

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
    
    cout << "Original Array: ";
    for(int i=0; i<n; i++){
        cout << arr[i] << " " ;
    }
    
    int i, j, temp;
    for(int i=0; i<n-1; i++){
        for(j=0;j<n-1-i;j++){
            if(arr[j]>arr[j+1]){
                temp =arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    
    cout << "\nSorted Array: ";
    for(int i=0; i<n; i++){
        cout << arr[i] << " " ;
    }
    
    return 0;
}

// Output

// Enter the number of elements: 5
// Enter elements: 1 0 2 5 3 
// Original Array: 1 0 2 5 3 
// Sorted Array: 0 1 2 3 5 