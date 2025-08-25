#include <stdio.h>

int main() {
    FILE *f = fopen("count.txt","w+");
    fputs("Welcome to the class of C and DSA",f);
    rewind(f);
    int count =0;
    
    while((fgetc(f)) != EOF)
        count++;

    printf("%d",count);
    
    fclose(f);
    return 0;
}