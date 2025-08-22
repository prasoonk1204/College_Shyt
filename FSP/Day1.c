#include <stdio.h>

int main() {
    int i=5,j,k,l,a,b;
    j=++i + ++i + ++i + ++i ;
    printf("%d %d",i,j);
    i=5;
    k= --i - --i - --i - --i;
    printf("\n%d %d",i,k);
    i=5;
    l= ++i - --i - --i - --i;
    printf("\n%d %d",i,l);
    
    a=015+ 0x71 +5;
    printf("\n%d",a);
    
    a=2,3,4;
    b=5,7,9;
    printf("\n%d",a+b);
    
    a=2;
    if(a--,--a,a)
        printf("\nThe Dalai Lama");
    else
        printf("\nJim Rogers");
        
    int movie=1;
    printf("\n");
    // 1<<3
    // 0001 :shift 1 3 place
    //1000: (8)10
    switch(movie<<2+movie){
        default:printf("3 idiots");
        case 4: printf("Gajni");
        case 5:printf("Krish");
        case 8:printf("Prasoon");
    }
    return 0;
}
