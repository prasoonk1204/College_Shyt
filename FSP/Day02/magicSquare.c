#include <stdio.h>

int main() {
    int i, j, n;
    printf("Enter no. of rows and columns: ");
    scanf("%d", &n);

    int a[n][n];
    for (i = 0; i < n; i++){
        for (j = 0; j < n; j++){
            a[i][j] = 0;
        }
    }

    int num = 1;
    i = 0;
    j = n / 2;
    while (num <= n * n) {
        if (i < 0 && j == n) {
            i += 2;
            j--;
        } else {
            if (i < 0){
                i = n - 1;
            } 
            if (j == n){
                j = 0;
            } 
        }
        if (a[i][j] != 0) {
            i += 2;
            j--;
            continue;
        } else {
            a[i][j] = num++;
        }
        i--;
        j++;
    }

    printf("Output:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            printf("%4d ", a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
