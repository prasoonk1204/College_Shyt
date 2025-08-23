#include <stdio.h>

int main() {
    
    printf("Enter the number of rows: ");
    int n;
    scanf("%d", &n);
    
    for (int i=0; i<n; i++){
        for (int j=n-1-i; j>0; j--){
            printf("  ");
        }
        for (int k=0; k<=i; k++){
            printf(" *");
        }
        for (int l=1; l<=i; l++){
            printf(" *");
        }
        printf("\n");
    }
    // n-i
    // 2*i-1
    //////////////////////////////////////////
    printf("\n");
    
    for (int i = 0; i < 2 * n - 1; i++) {
        int comp;
        if (i < n) {
            comp = 2 * (n - i) - 1;
        } else{
            comp = 2 * (i - n + 1) + 1;
        }
        for (int j = 0; j < comp; j++){
            printf(" ");
        }
        for (int k = 0; k < 2 * n - comp; k++){
            printf("* ");
        }
        printf("\n");
    }
    
    //////////////////////////////////////////
    printf("\n");
    
    for (int i = 1; i <= n ; i++) {
        for (int j = 1; j <= i; j++){
            printf("%d",(j%2));
        }
        printf("\n");
    }
    
    //////////////////////////////////////////
    printf("\n");
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            if ((i + j) % 2 == 0)
                printf("1");
            else
                printf("0");
        }
        printf("\n");
    }

    //////////////////////////////////////////
    printf("\n");
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i==1 || j==1 || i==n || j==n)
                printf("* ");
            else
                printf("  ");
        }
        printf("\n");
    }

    return 0;
}
