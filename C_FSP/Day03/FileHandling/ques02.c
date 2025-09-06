#include <stdio.h>

int main() {
    FILE *f = fopen("name.txt","w+");
    fprintf(f,"12345678");
    rewind(f);
    char ch;
    
    while((ch=fgetc(f)) != EOF)
        printf("%c",ch);
    
    fclose(f);
    return 0;
}