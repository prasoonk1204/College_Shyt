// 5. Count Even and Odd Numbers in an Array

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

    int evenCount = 0, oddCount = 0;

    for(int i = 0; i < n; i++) {
        if(arr[i] % 2 == 0)
            evenCount++;
        else
            oddCount++;
    }

    cout << "Number of even elements: " << evenCount << endl;
    cout << "Number of odd elements: " << oddCount << endl;

    return 0;
}

// Output

// Enter the number of elements: 7
// Enter elements: 10 11 32 33 45 68 55
// Number of even elements: 3
// Number of odd elements: 4