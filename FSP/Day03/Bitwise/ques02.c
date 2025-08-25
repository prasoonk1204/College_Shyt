#include <stdio.h>

int main() {
    int n,i;
    printf("Enter number and bit position to set: ");
    scanf("%d %d",&n,&i);
    
    n |= (1<<i);
    printf("Number after setting %d-th bit: %d\n",i,n);
    
    return 0;
}