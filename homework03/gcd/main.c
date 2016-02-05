#include <stdio.h>
#include <stdlib.h>

extern int gcd(int, int);

int main(int argc, char *argv[]) {
    if (argc != 3) {
    	fprintf(stderr, "usage: %s a b\n", argv[0]);
    	return EXIT_FAILURE;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    printf("gcd(%d, %d) = %d\n", a, b, gcd(a, b));

    return EXIT_SUCCESS;
}
