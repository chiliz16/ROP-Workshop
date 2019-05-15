#include <stdio.h>
#include <unistd.h>	

int main()
{   
    // distable buffering for network transmission
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    // vulnerable code
    char data[20];
    int n = 0; 
    printf("Give me the Code: \n");
    n = read(STDIN_FILENO, data, 0x60);
    printf("You gave me: %s", data);
    return 0;	
}
