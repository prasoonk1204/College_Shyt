#include <stdio.h>

int main() {
    FILE *f = fopen("file.txt","w+");
    if(f==NULL){
        printf("Error opening file..\n");
        return 1;
    }

    fprintf(f,"0123456789\n");
    fprintf(f,"abcdefgh\n");

    fseek(f, 0, SEEK_SET);   
    fprintf(f,"ABC"); 
    
    fseek(f, 1, SEEK_CUR);   
    fprintf(f,"D"); 

    fclose(f);
    return 0;
}
