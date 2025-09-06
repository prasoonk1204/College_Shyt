#include <stdio.h>

int main() {
    int i ,n,sum=0,p=1;
    printf("Enter no. of terms: ");
    scanf("%d", &n);
    
    for (i = 1; i <= n; i++) {
        p=p*i;
        sum=sum+p;
    }
    
    printf("\nOutput: %d",sum);
    return 0;
}
