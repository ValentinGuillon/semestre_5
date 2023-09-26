#include <stdio.h>
#include <stdlib.h>



//affiche un entier (entre 0 et 999) à droite, sur 4 caractères 
void aff_value(int value) {
    if (value > 99) printf(" ");
    else if (value > 9) printf("  ");
    else printf("   ");
    printf("%d", value);
}


// =====================
// EXO 2
// A
//calcule le résultat d'UN SEUL couple k n, récursivement
int triangle_rec(int k, int n) {
    if (k == 0 || n == k) return 1;
    return triangle_rec(k-1, n-1) + triangle_rec(k, n-1);
}


// B
//calcule TOUS les résultat tous les couples k n, et place le résultat de chacun dans un tableau de taille n*n
void triangle_it(int** tab, int n) {
    tab[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        tab[i][0] = 1;
        for (int j = 1; j <= n; j++) {
            if (j > n) tab[i][j] = 0;
            else tab[i][j] = tab[i-1][j-1] + tab[i-1][j];
        }
    }
}



void aff(int **tab, int n) {
    //decoration
    //printf("  n\\k|");
    //for (int i = 0; i <= n; i++) aff_value(i);
    //printf("\n");

    //parcours et affichage des éléments de la matrice (uniquement quand i <= j)
    for (int i = 0; i <= n; i++) {
        //aff_value(i); printf(" |"); //decoration
        // for (int j = 0; j <= n; j++) {
        for (int j = 0; j <= i; j++) {
            aff_value(tab[i][j]);
        }
        printf("\n");
    }
}


// D
int factorielle_rec(int x) {
    if (x <= 1) return 1;

    return x * factorielle_rec(x-1);
}


int factorielle(int x) {
    int result = 1;

    for (int i = 2; i <= x; i++) result *= i;
    return result;
}

int triangle_fact(int k, int n) {
    return factorielle(n) / (factorielle(k) * factorielle(n-k));
}



// =====================





void A(int k, int n) {
    printf("\nEXO2 A\n");

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= i; j++) {
            int value = triangle_rec(j, i);
            aff_value(value);
        }
        printf("\n");
    }
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


void D(int k, int n) {
    printf("\nEXO2 D\n");
    printf("%d\n", triangle_fact(k, n));
}


void exo2(void) {
    
    int n = 7;
    int k = 3;
    
    printf("k = %d, n = %d\n", k, n);

    A(k, n);
    B(n);
    C(k, n);
    D(k, n);
    
}


int main(void) {
    exo2();
}






