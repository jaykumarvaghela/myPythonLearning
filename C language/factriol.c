#include<stdio.h>
#include<conio.h>


int main(){
    int n,tmp=1;
    printf("Enter a number ");
    scanf("%d", &n);
    for(int i=1;i<=n;i++){
        tmp = i*tmp;
    }
    printf("%d", tmp);
    return 0;
}