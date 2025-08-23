#include <stdio.h>

int main() {
    int i,j,n,k=1;
    printf("Enter no. of rows and columns: ");
    scanf("%d",&n);
    
    int a[n][n];
    
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            a[j][i]=k;
            k++;
        }
    }
    
    printf("Output: \n");
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%4d ",a[i][j]);
        }
        printf("\n");
    }
    return 0;
}