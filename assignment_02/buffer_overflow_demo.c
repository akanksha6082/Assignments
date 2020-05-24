#include<stdio.h>
#include<string.h>

int main(int argc, char *argv[])
{
	char buff[256];
	strcpy(buff, argv[1]);
	printf("%s", buff);
	return 0;
}
