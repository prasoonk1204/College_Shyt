#include <stdio.h>

int main() {
    FILE *f = fopen("data.txt","r+");
    if(f==NULL)
        printf("File not found\n");
    else 
        printf("Opened\n");
    fclose(f);
    return 0;
}