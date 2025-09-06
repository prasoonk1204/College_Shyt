#include <stdio.h>

int main() {
    int i ,n,sum=0;
    printf("Enter no. of terms: ");
    scanf("%d", &n);
    
    printf("The Series is: \n");
    for (i = 1; i <= n; i++) {
        if(i%2==0 && i!= n){
            printf(" 7 +");
            sum+=7;
        }else if(i%2==1 && i!= n) {
            printf(" 4 +");
            sum+=4;
        } else {
            if(i%2==0){
                printf(" 7 ");
                sum+=7;
            } else {
                printf(" 4 ");
                sum+=4;
            }
        }
    }
    
    printf("\n\nFinal result: %d",sum);
    return 0;
}

// Enter no. of terms: 5
// The Series is: 
//  4 + 7 + 4 + 7 + 4 

// Final result: 26