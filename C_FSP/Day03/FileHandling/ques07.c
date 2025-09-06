#include<stdio.h>
#include<string.h>
int main() {
	FILE *f ;
    int l,i;
char data[25]="Learning is Essential";
l=strlen(data);
f = fopen("new.txt","w");
if(f == NULL)
{
	printf("Unable to create or open the file...");
}
else
{
	for(i=0;i<l;i++)
	{
	printf("Writing the character %c \n",data[i]);
	fputc(data[i],f);
    } 
	printf("Data written to the file successfully...");
	fclose(f);
}
 return 0;
}