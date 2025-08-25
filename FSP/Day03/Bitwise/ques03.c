#include <stdio.h>

// Function prototype
int missing(int a[], int n);

int main()
{
    int a[] = {1, 2, 3, 4};
    int x = 5, f;

    f = missing(a, x);
    printf("Missing no is: %d\n", f);

    return 0;
}

int missing(int a[], int n)
{
    int x1 = 0, x2 = 0, i;

    for (i = 0; i < n - 1; i++)
        x2 ^= a[i];

    for (i = 1; i <= n; i++)
        x1 ^= i;

    return x1 ^ x2;
}
