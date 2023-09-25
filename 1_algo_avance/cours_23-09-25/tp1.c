#include <stdio.h>
#include <stdlib.h>






int triangle_rec(int k, int n) {
    if (k == 0 || n == k) return 1;
    return triangle_rec(k-1, n-1) + triangle_rec(k, n-1);
}


void triangle_it(int** tab, int k, int n) {
    tab[0][0] = 1;
    for (int i = 1; i < n; i++) {
        tab[i][0] = 1;
        for (int j = 1; j < i; j++) {
           tab[i][j] = tab[i-1][j-1] + tab[i-1][j];
        }
    }
}



void aff(int **tab, int k, int n) {

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            printf("%d, ", tab[i][j]);
        }
        printf("\n");
    }
}






int main(void) {
    printf("%d\n", triangle_rec(2, 3));
    
    int n = 8;
    int k = 3;
    
    int **tab;
    
    tab = malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        tab[i] = malloc(k * sizeof(int));
        for (int j = 0; j < k; j++) {
            tab[i][j] = 0;
        }
    }
    
    
    
    triangle_it(tab, k, n);
    aff(tab, k, n);
    
    
    
    
}






