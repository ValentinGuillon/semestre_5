
#include <stdio.h>
#include<stdlib.h>
#include<time.h>
#include<assert.h>
#include<string.h>

#define MAX 2000


typedef unsigned char uchar;
typedef unsigned char monplan [MAX][MAX];




void affiche (int sizex, int sizey, monplan pl) {
    int i, j;
    for(j = sizey; j >= 0; j--) {
        for (i = 0; i <= sizex; i++)
            printf("%c", pl[i][j]);
        printf("\n");
  }
}

// Fonction qui calcule les coordonnées de la droite discrète par l'algo trivial.
void droite_triviale (int dx, int dy){
    int x, y;
    float z;
    for (x = 0; x <= dx; x++) {
        z = ((float) x * dy / dx) + 0.5;
        y = (int) z;
    }
}

// Fonction qui permet d'afficher le résultat obtenu dans le plan pl.
void droite_triviale_verif (int dx, int dy, monplan pl) {
    int x, y;
    for (x = 0; x <= dx; x++) {
        y = (int) (((float) x * dy / dx) + 0.5);
        pl [x][y] = '.';
  }
}






void droite_br(int dx, int dy) {
    int delta, incH, inc0;
    incH = -dy -dy;
    delta = incH + dx;
    inc0 = delta + dx;
    for (int x = 0, y = 0; x <= dx; x++) {
        if (delta <= 0) {
            y++;
            delta += inc0;
        }
        else {
            delta += incH;
        }
    }
}


void droite_br_verif(int dx, int dy, monplan pl) {
    int delta, incH, inc0;
    incH = -dy -dy;
    delta = incH + dx;
    inc0 = delta + dx;
    for (int x = 0, y = 0; x <= dx; x++) {
        //afficher(x, y);
        pl[x][y] = '.';
        if (delta <= 0) {
            y++;
            delta += inc0;
        }
        else {
            delta += incH;
        }
    }
}






void droite_rvw_verif(int dx, int dy, monplan pl) {
    int delta, incH, inc0;
    incH = -dy -dy;
    delta = incH + dx;
    inc0 = delta + dx;

    int octant_part;
    if (dx < (2 * dy) {
        octant_part = 1;
    }
    else 
    


    for (int x = 0, y = 0; x <= dx; x+=2) {
        //afficher(x, y);

        if (delta <= 0) {
            y++;
            delta += inc0;
        }
        else {
            delta += incH;
        }
        pl[x][y] = '.';
        
    }
}




int compare_time(void) {
    int dx = 100, dy = 100;
    clock_t t_before, t_after;
    
    printf("Temps des algos:\n");
    
    //trival
    t_before = clock();

    for (int x = 0; x < dx; x++) {
        for (int y = 0; y < dy; y++) {
            droite_triviale (x, y);
        }
    }
    t_after = clock();
    printf("trival = %d\n", t_after - t_before);

    //br
    t_before = clock();

    for (int x = 0; x < dx; x++) {
        for (int y = 0; y < dy; y++) {
            droite_br (x, y);
        }
    }
    t_after = clock();
    printf("br = %ld\n", t_after - t_before);
}







int main (int argc, char ** argv) {
    int sizex, sizey, dx, dy, i, j;
    monplan plan;
    clock_t t0, t1, dt;
    dx = 100;
    dy = 100;
    if (argc == 3){
        dx = atoi (argv[1]);
        dy = atoi (argv[2]);
    }
    if (dx < 0)
        dx = 0 - dx;
    if (dy < 0)
        dy = 0 - dy;
    if (dx < dy) {
        dx += dy;
        dy = dx - dy;
        dx = dx - dy;
    } /* nous restons dans le premier octant */
    if (dx >= MAX)
        dx = MAX - 1;
    if (dy >= MAX)
        dy = MAX - 1;

    memset (plan, ' ', MAX*MAX);
    droite_triviale_verif (11, 3, plan);
    printf("Triviale\n");
    affiche(11, 3, plan);
    memset(plan, ' ', MAX*MAX);
    droite_triviale_verif (24, 10, plan);
    affiche (24, 10, plan);
    /* Test des fonctions */
    memset (plan, ' ', MAX*MAX);
    printf("\n \n");
    printf("Bresenham\n");
    droite_br_verif (11, 3, plan);
    affiche (11, 3, plan);
    memset (plan, ' ', MAX*MAX);
    droite_br_verif (24, 10, plan);
    affiche (24, 10, plan);
    // memset (plan, ' ', MAX*MAX);
    // printf("\n \n");
    // printf("Rokne \n");
    // droite_rvw_verif (11, 3, plan);
    // affiche (11, 3, plan);
    // memset (plan, ' ', MAX*MAX);
    // droite_rvw_verif (24, 10, plan);
    // affiche (24, 10, plan);
    
    //compare_time();
 
}


