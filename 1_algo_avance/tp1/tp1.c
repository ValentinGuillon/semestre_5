#include <stdio.h>
#include <stdlib.h>
#include<time.h>

#define N 7
#define K 3
#define VITESSE_AUGMENTATION_N 5


typedef struct Vector_T {
    int max_size;
    int size;
    int *tab;
} Vector;

//affiche un entier (entre 0 et 99999) à droite, sur 4 caractères 
void aff_value(int value) {
    if (value > 9999) printf(" ");
    else if (value > 999) printf("  ");
    else if (value > 99) printf("   ");
    else if (value > 9) printf("    ");
    else printf("     ");
    printf("%d", value);
}

void init_vector(Vector* vec, int max) {
    vec->max_size = max;
    vec->size = 0;
    vec->tab = malloc(max * sizeof(int));
}

void print_vector_tab(Vector* vec) {
    for (int i = 0; i < vec->size; i++) {
        aff_value(vec->tab[i]);
    }
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
void triangle_it_2d(int** tab, int n) {
    // ligne de 0 à n
    for (int i = 0; i <= n; i++) {
        // colonne de 0 à i
        for (int j = 0; j <= i; j++) {
            if (j == 0 || j == i)
                tab[i][j] = 1;
            else
                tab[i][j] = tab[i-1][j-1] + tab[i-1][j];
        }
    }
}


void print_tab_2d(int **tab, int n) {
    //decoration
    //printf("  n\\k|");
    //for (int i = 0; i <= n; i++) aff_value(i);
    //printf("\n");

    //parcours et affichage des éléments de la matrice (uniquement quand i <= j)
    for (int i = 0; i <= n; i++) {
        //aff_value(i); printf(" |"); //decoration
        for (int j = 0; j <= i; j++) {
            aff_value(tab[i][j]);
        }
        printf("\n");
    }
}



// C
void triangle_it_vector(int n) {
    Vector vec;
    init_vector(&vec, n+1);


    for (int i = 0; i <= n; i++) {
        for (int j = i; j >= 0; j--) {
            if (j == 0) {
                vec.tab[j] = 1;
            }

            else {
                vec.tab[j] += vec.tab[j - 1];
            }
        }
        vec.size += 1;
        print_vector_tab(&vec);
        printf("\n");
    }
}





// D
int factorielle_rec(int x) {
    if (x <= 1) return 1;

    return x * factorielle_rec(x-1);
}


// int factorielle(int x) {
//     int result = 1;

//     for (int i = 2; i <= x; i++) result *= i;
//     return result;
// }

void triangle_fact(int n) {

    aff_value(1); //k == 0 && n == 0
    printf("\n");
    for (int i = 1; i <= n; i++) {
        aff_value(1); //k == 0
        for (int j = 1; j < i; j++) {
            aff_value(factorielle_rec(i) / (factorielle_rec(j) * factorielle_rec(i-j)));
        }
        aff_value(1);
        printf("\n");
    }
}



// =====================





void A(int n) {
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
    
    
    
    triangle_it_2d(tab, n);
    print_tab_2d(tab, n);
}

void C(int n) {
    printf("\nEXO2 C\n");
    triangle_it_vector(n);
}


void D(int n) {
    printf("\nEXO2 D\n");
    triangle_fact(n);
}


void exo2(void) {
    
    printf("k = %d, n = %d\n", K, N);

    A(N);
    B(N);
    C(N);
    D(N);
    
}



void test_time(int *resultat, int n){
    resultat[0] = n;
    // int nb_exos = 4;
    // char *exos[20] = {"recursif", "itératif 2D", "itératif vecteur", "factorielle"};
    // int resultats[4];
    clock_t time_before, time_after;

    int i = 1;

    time_before = clock();
    A(n);
    time_after = clock();
    resultat[i++] = (int) time_after - time_before;

    time_before = clock();
    B(n);
    time_after = clock();
    resultat[i++] = (int) time_after - time_before;

    time_before = clock();
    C(n);
    time_after = clock();
    resultat[i++] = (int) time_after - time_before;

    time_before = clock();
    D(n);
    time_after = clock();
    resultat[i++] = (int) time_after - time_before;
}





int main(void) {
    // only calculs and printing
    // exo2();


    // calculs, printing and time
    int nb_tests = 5;

    char *exos[20] = {"          N", "   recursif", "     ité 2D", "ité vecteur", "factorielle"};
    int **resultats;
    resultats = malloc(nb_tests * sizeof(int*));
    for (int i = 0; i < nb_tests; i++) {
        resultats[i] = malloc(5 * sizeof(int));
    }
    
    for (int i = 0, j = 1; i < nb_tests; i++, j += VITESSE_AUGMENTATION_N) {
        test_time(resultats[i], j);
    }

    printf("\n");
    for (int j = 0; j < 5; j++) {
        printf("%s", exos[j]);
        for (int i = 0; i < nb_tests; i++) {
            printf("\t%d", resultats[i][j]);
        }
        printf("\n");
        
    }

}




