#include<stdio.h>
#include<string.h>
int main() {
	FILE *f ;
    char name[25];
    int age;
printf("Enter your name and age :\n");
scanf("%s %d",name,&age);
f = fopen("doc.txt", "a");
if(f == NULL)
{
	printf("Unable to create or open the file...");
}
else
{
    fprintf(f,"%s \t %d\n",name,age);
    printf("Data written to the file successfully...");
	fclose(f);
}
 return 0;
}