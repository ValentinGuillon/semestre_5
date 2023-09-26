#include <stdio.h>
#include <stdlib.h>





// =====================
// EXO 2
// A
int triangle_rec(int k, int n) {
    if (k == 0 || n == k) return 1;
    return triangle_rec(k-1, n-1) + triangle_rec(k, n-1);
}


// B
void triangle_it(int** tab, int n) {
    tab[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        tab[i][0] = 1;
        for (int j = 1; j <= n; j++) {
            if (j > n) tab[i][j] = 0;
            else tab[i][j] = tab[i-1][j-1] + tab[i-1][j];
        }
        // tab[i][i] = 1;
    }
}


void aff_value(int value) {
    if (value > 99) printf(" ");
    else if (value > 9) printf("  ");
    else printf("   ");
    printf("%d", value);
}

void aff(int **tab, int n) {
    //decoration
    printf("  n\\k|");
    for (int i = 0; i <= n; i++) aff_value(i);
    printf("\n");

    //parcours et affichage des éléments de la matrice (uniquement quand i <= j)
    for (int i = 0; i <= n; i++) {
        aff_value(i); printf(" |"); //decoration
        // for (int j = 0; j <= n; j++) {
        for (int j = 0; j <= i; j++) {
            aff_value(tab[i][j]);
        }
        printf("\n");
    }
}

// =====================





void A(int k, int n) {
    printf("\nEXO2 A\n");
    printf("%d\n", triangle_rec(k, n));
}

void B(int n) {
    printf("\nEXO2 B\n");
    int **tab;
    
    tab = malloc((n+1) * sizeof(int *));
    for (int i = 0; i <= n; i++) {
        tab[i] = malloc((n+1) * sizeof(int));
    }
    
    
    
    triangle_it(tab, n);
    aff(tab, n);
}

void C(int k, int n) {
    printf("\nEXO2 C\n");
    printf("NOT WRITE\n");
}


void exo2(void) {
    
    int n = 6;
    int k = 3;
    
    printf("n = %d, k = %d\n", n, k);

    A(k, n);
    B(n);
    C(k, n);
    
}


int main(void) {
    exo2();
}






