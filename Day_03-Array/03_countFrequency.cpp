// 3. Count Frequency of Each Element

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

    cout << "Frequency of each element:\n";

    for (int i = 0; i < n; i++) {
        // Check if this element is already counted
        bool visited = false;
        for (int j = 0; j < i; j++) {
            if (arr[i] == arr[j]) {
                visited = true;
                break;
            }
        }

        if (!visited) {
            int count = 1;
            for (int k = i + 1; k < n; k++) {
                if (arr[i] == arr[k]) {
                    count++;
                }
            }
            cout << arr[i] << " -> " << count << endl;
        }
    }

    return 0;
}

// Output

// Enter the number of elements: 5
// Enter elements: 1 1 5 6 3
// Frequency of each element:
// 1 -> 2
// 5 -> 1
// 6 -> 1
// 3 -> 1