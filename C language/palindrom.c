#include<stdio.h>

int main(){

    int n,m,tmp,rev=0;
    char res;
    
    printf("Enter the number");
    scanf("%d" ,&n);

    m=n;

    while (n!=0){
        tmp = n%10;
        rev = (rev*10)+tmp;
        n = n/10;
    }

    if(m!=rev){
        printf("not");
    }else{
        printf("Palindrom");
    }
    return 0;    
}