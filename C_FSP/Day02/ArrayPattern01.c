#include <stdio.h>

int main() {
    int i,j,n;
    printf("Enter no. of rows and columns: ");
    scanf("%d",&n);
    
    int a[n][n];
    
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(i>=j){
                a[i][j]=i;
            } else {
                a[i][j]=j;
            }
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