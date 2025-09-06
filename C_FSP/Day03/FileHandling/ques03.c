#include <stdio.h>

int main() {
    FILE *f = fopen("log.txt","a");
    fprintf(f,"Hello World");
    rewind(f);
    char ch;
    ch=fgetc(f);
    printf("%c",ch);
    fclose(f);
    return 0;
}