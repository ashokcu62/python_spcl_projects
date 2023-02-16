#include <stdio.h>
#include <math.h>


int main()

{
    int n = 3;
    int i, r, j, c, k;
    for (i = 1; i <= n; i++)
    {
        for (r = 1; r <= i; r++)
        {
            for (c = 1; c <= 2; c++)
            {
                printf("X");
            }
            printf("\n");
        }
        for (j = 1; j <= i; j++)
        {
            printf("_");
        }
        for (k = 1; k <= 2*i; k++)
        {
            printf("X");
        }
        printf("\n");
    }
}
