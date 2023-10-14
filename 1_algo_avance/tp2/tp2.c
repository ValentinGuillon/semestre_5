
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
    int x;
    int y;
    float z;
    for (x = 0; x <= dx; x++) {
        z = (int) (((float) x * dy / dx) + 0.5);
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






void follow_pattern(int pattern, int *x, int *y, monplan pl) {
    for (int step = 1; step <= 2; step++) {
        switch (pattern) {
            // case 1:
            //     break;
            case 2:
                if (step == 2) (*y)++;
                break;
            case 3:
                if (step == 1) (*y)++;
                break;
            case 4:
                (*y)++;
                break;
            
            default:
                break;
        }

        (*x)++;
        pl[*x][*y] = '.';
    }


    // int i = 2;

    // while (i > 0) {
    //     if (i == 2) {
    //         if (pattern == 3 || pattern == 4) {
    //             (*y)++;
    //         }
    //     }
    //     if (i == 1) {
    //         if (pattern == 2 || pattern == 4) {
    //             (*y)++;
    //         }
    //     }
    //     (*x)++;
    //     pl[*x][*y] = '.';
    // }
}



void droite_rvw_verif(int dx, int dy, monplan pl) {
    int delta, incH, inc0;
    incH = -dy -dy;
    delta = incH + dx;
    inc0 = delta + dx;

    //int octant_part;
    if (dx < (2 * dy)) {
        //octant_part = 1;
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




void compare_time(void) {
    int dx = 100, dy = 100;
    clock_t t_before, t_after;
    
    printf("Temps des algos: (pour tout les couples x/y avec x et y entre 0 et 100\n");
    
    //trival
    t_before = clock();

    for (int x = 0; x < dx; x++) {
        for (int y = 0; y < dy; y++) {
            droite_triviale (x, y);
        }
    }
    t_after = clock();
    printf("trival = %ld\n", t_after - t_before);

    //Bresenham
    t_before = clock();

    for (int x = 0; x < dx; x++) {
        for (int y = 0; y < dy; y++) {
            droite_br (x, y);
        }
    }
    t_after = clock();
    printf("br = %ld\n", t_after - t_before);
}







//int main (int argc, char ** argv) {
int main (void) {
    //int sizex, sizey;
    int dx, dy;
    //int i, j;
    monplan plan;
    //clock_t t0, t1, dt;
    dx = 100;
    dy = 100;
    //if (argc == 3){
    //    dx = atoi (argv[1]);
    //    dy = atoi (argv[2]);
    //}
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


    /* Test des fonctions */
    //droite trivial 11 3
    printf("Triviale\n");
    memset (plan, ' ', MAX*MAX);
    droite_triviale_verif (11, 3, plan);
    affiche(11, 3, plan);
    //droite trivial 24 10
    memset(plan, ' ', MAX*MAX);
    droite_triviale_verif (24, 10, plan);
    affiche (24, 10, plan);

    //droite Brensenham 11 3
    printf("\n\nBresenham\n");
    memset (plan, ' ', MAX*MAX);
    droite_br_verif (11, 3, plan);
    affiche (11, 3, plan);
    //droite Brensenham 24 10
    memset (plan, ' ', MAX*MAX);
    droite_br_verif (24, 10, plan);
    affiche (24, 10, plan);



    //droite pas de deux 11 3
    // memset (plan, ' ', MAX*MAX);
    // printf("\n\nRokne \n");
    // droite_rvw_verif (11, 3, plan);
    // affiche (11, 3, plan);
    //droite pas de deux 24 10
    // memset (plan, ' ', MAX*MAX);
    // droite_rvw_verif (24, 10, plan);
    // affiche (24, 10, plan);
    
    compare_time();
 
}

/*
procedure LINE(a1, b1, a2, b2: integer);
var dx, dy, incr1, incr2, D, x, y, xend, c: integer;

    procrdure draw(pattern: integer);
    begin
        case pattern of
            1: ++x; point(x, y); ++x; point(x, y);
            2: ++x; point(x, y); ++x; ++y ; point(x, y);
            3: ++x; ++y ;point(x, y); ++x; point(x, y);
            4: ++x; ++y ; point(x, y); ++x; ++y ; point(x, y);
            end {case}
        end {draw}
    
    begin
        dx = a2 - a1; dy = b2 - b1;
        x = a1; y = b1;
        if dx is even then begin parity = 0; xend = a2; end
        else begin parity = 1; xend = a2 - 1; end;
        point(x, y);
        if incr2 < 0 then begin
            c = 2*dy;
            incr1 = 2*c;
            D = incr1 -dx;
            while x <> xend do
                if D < 0 then begin
                    draw(1); D = D + incr1; end
                else begin
                    if D < c then draw(2) else draw(3);
                    D = D + incr2;
                    end;
            end
        else begin
        c = 2 * (dy - dx);
        incr1 = 2 * c;
        D = incr1 + dx;
        while x <> xend do
            if D >= 0 then begin
                draw(4): D = D + incr1; end
            else begin
                if D < c then draw(2) else draw(3);
                D = D + incr2;
                end;
        end; {if}
        if parity = 1 then point(a2, b2);
    end; {LINE}

*/




/*

procedure LINE(a1, bl, a2, b2: integer);
var dx, dy, incrl, incr2, D, x, y, xend, c: integer;
Pattem 1
Pattern 2
procedure draw(pattem: integer);
begin
case pattern of
1: +tX; point(x. y); +tx; point(x. y);
2: +tx; point(x, y); i-l-x; +ty; point(x, y);
3: +tx; +t-y; poillt(x, y); ++x; point(x, y);
4: ++x; ++y; point(x, y); +tx; +ky; point(x. y);
end (case)
end (draw)

...


begin
    dx=a2-al; dy=b2-bl;
    x=al; y=bl;
    if dx is even then begin parity = 0;: xend = a2; end
    else begin parity = 1; xend = a2 - 1; end;
    point(x. y);
    incr2 = 4*dy - 2*dx;
    if incr2 < 0 then begin (slope is less than l/2)
        c = 2*dy;
        incrl = 2*c;
        D=incrl -dx;
            while x o xend do
            if D c 0 then begin
                draw(l); D = D + incrl; end
            else begin
                if D < c then draw(2) else draw(3);
                D=D+incr2;
                end:
        end
else begin
(slope is 2 l/2)
c = 2*(dy - dx);
incrl = 2*c;
D=incrl+dx;
while x c> xend do
*/
