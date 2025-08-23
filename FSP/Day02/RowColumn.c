#include <stdio.h>

int main() {
    int i,j,n;
    printf("Enter no. of rows and columns: ");
    scanf("%d",&n);
    
    int a[n][n];
    
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(i==j && i+j==n-1){
                a[i][j] = 30;
            } else if(i==j){
               a[i][j] =10; 
            } else if(i+j==n-1) {
                a[i][j] = 20;
            } else {
                a[i][j]=0;
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

// Enter no. of rows and columns: 5
// Output: 
//   10    0    0    0   20 
//    0   10    0   20    0 
//    0    0   30    0    0 
//    0   20    0   10    0 
//   20    0    0    0   10 