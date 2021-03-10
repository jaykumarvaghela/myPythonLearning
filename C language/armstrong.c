#include<stdio.h>

int main(){

    int n,tmp,arm=0,nub;

    printf("Enter the number");
    scanf("%d", &n);
    nub = n;
    while(n!=0){
        tmp = n%10;
        arm = arm+(tmp*tmp*tmp);
        n=n/10;
    }

    if(arm==nub){
        printf("Armstrong");
    }else{
        printf("Not");
    }
}