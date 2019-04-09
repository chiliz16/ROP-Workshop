#include <stdio.h>
#include <unistd.h>	

int main()
{
    char data[20];
	int n = 0; 
	printf("Give me the Code: \n");
	n = read(STDIN_FILENO, data, 0x40);
	data[n] = 0;
	printf("You gave me: %s", data);
	return 0;	
}
