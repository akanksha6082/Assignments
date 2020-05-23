#include<stdio.h>

int factorial(int );

int factorial(int n)
{
	if(n == 1 )
		return 1;
	else
		return(n * factorial(n-1));
}


int main()
{
	int n = 5;
	int fact = factorial(n);
	printf("%d", fact);
	return 0;
}