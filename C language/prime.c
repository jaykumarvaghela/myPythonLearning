#include<stdio.h>

int main(){
    int n,p=1;

    printf("Enter the number");
    scanf("%d", &n);
    for(int i=2; i<=n/2; i++){
        if(n%i==0){
            p=0;
            break;
        }
    }
    if (p==1){
        printf("Prime");   
    }else{
        printf("Not Prime");
    }
}