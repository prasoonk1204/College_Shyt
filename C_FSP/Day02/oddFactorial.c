#include <stdio.h>

int main() {
    int i ,n,sum=0,fact=1;
    printf("Enter no. of terms: ");
    scanf("%d", &n);
    
    for (i = 1; i <= n; i++) {
        sum+=fact;
        printf("\n\t\t Current i=%d, fact=%d, and sum=%d",2*i-1,fact,sum);
        fact=fact*(2*i)*(2*i+1);
    }
    
    printf("\n\nFinal result: %d",sum);
    return 0;
}
