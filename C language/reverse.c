#include<stdio.h>

int main(){
    
    int n,rev=0,tmp;

    printf("Enter the number ");
    scanf("%d", &n);

    while (n != 0){
        tmp=n%10;
        rev = rev*10+tmp;
        n=n/10;
    }

    printf("%d", rev);   
    
    return 0;
}