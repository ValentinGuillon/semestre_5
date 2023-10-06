# Interpretation et Compilation
# L2-B
# GUILLON Valentin, 20002588

# Contient les réponse aux question du TP2, ainsi que le programme de l'exo 2
# Le prog est executable sans problème

# J'ai mal compris l'exo 2
# J'ai cru que c'était "la somme, des nombres premiers, dans les n premiers entiers"...


#Exo 0
#   3. Le prog tente d'aller au label "main", mais ne peut pas, car il n'existe pas (aucun fichier n'a été chargé)
#   5. Visuellement, il ne se passe rien (concrètement, mains est bien appelé, mais la seul instruction qu'il contient et de revenir à l'adresse de la fonction appelante (donc hors du main.s, je crois)
#   6. Bah rien wtf
#   7. a. On ne dit que le label "main" existe déjà (car main.s est tjr chargé, il faut réinitialiser d'abord, avec "reinit")
#   8. ligne...
#        5: je ne sais pas
#        6: charge 42 dans le registre $t0
#        7:   --      9    --             $t1
#        8: met la somme des registres $t0 et $t1 dans $t2
#        9: déplace le contenu de $t0 dans $a0
#       10: on charge 1 dans $v0
#       11: syscall execute une certain manip en fonction de se que contient $v0 (dans ce cas si, $v0 contient 1, ce qui fait un print)
#       12: jump vers l'adresse dans $ra ("fonction" appelante de main)
#       ... des bails hors de "basic.s"

#Exo 1
#   1. Fait
#   2. Il semblerait que syscall 5 stock la valeur dans $v0 (c'est dans le cours, et ça se comprends dans le programme (avec move $t0 $v0, alors qu'en théorie, on écrit dans $v0)
#   3. on est bloqué dans le prog
#   4. ça boucle dans main (à cause de $ra qui est écrasé lors du jump vers "add_user_num", mais de retour dans "main", $ra ne correspond plus à l'"appellant" de main, mais à "main" lui même)
#   5. technique de shlagos. avant de jump vers "add_user_num", on stocke $ra (dans $s7 par exemple), en après le jump, on rétabli $ra (qui est dans $s7)
#   6. Problème. Si on écrase $s7 dans "add_user_num", bah on est niqué mdr
#   7. une pile (pas mon idée, mais une bonne idée), mais je vois pas comment (avec les 32 registres) faire cette pile
#   8.
#       6: charge 3 dans un registre temp (corresponfant au nombre de loop pour ce prog)
#      38: if conditionnelle. si le registre $t2 contient la même chose que $0 (donc zéro), on jump à un adress specifique
#      39: desincrement $t2
#      40: jump vers une adresse (pas besoin d'expliquer ce qu'elle fait)
#      41: on jump vers l'adresse du label "loop" (ligne 37)
#      Puis rebelotte (ligne 38 à 41, 3x)
#      La quatrième fois que la ligne 38 est lu, (donc que l'égalité est vrai), jump a label "end_loop" (ligne)
#      34: chargement de 10 dans $v0
#      35: quit le programme (car syscall 10, parcque 10 dans $v0)

#Exo 2

.text
.globl main

    #regiters shared through fonctions
# $s0 = résultat des n premiers entiers à partir de 0 (de 0 à n-1)
# $s1 = n
# $s2 = i
# $s3 = a (dans a % b)
# $s4 = b (dans a % b)
# $s6, bool pour i premier ou non (utilisé pour debug)



# $s3 % $s4 = $s3
modulo:
    # si $s3 <= 0
    blez $s3, modulo_end
    sub $s3, $s3, $s4
    b modulo
modulo_end:
    jr $ra


# on verifie si i ($s2) est premier
# si vrai, a l'ajoute dans $s0

add_next_premier:
    move $s7, $ra
    #li $s6, 0

    # $t1 = j (ou le diviseur de i)
    li $t0, 3 #commence à 2 et s'increment jusqu'à i-1 ($s2 -1)

    # si i <= 3 (si on se demande si un nombre plus petit ou égale à 3 est premier, il est premier)
    sub $t2, $s2, $t0
    blez $t2, anp_end_loop_true

    addi $t0, $t0, -1

anp_loop:
    # de 2 à i-1
    beq $t0, $s2, anp_end_loop_true

    # print "aled"
    #li $v0, 4
    #la, $a0, aled
    #syscall

    # i % j ($s2 % $t0)
    move $s3, $s2
    move $s4, $t0
    jal modulo

    # print i
    #li $v0, 1
    #move $a0, $s3
    #syscall
    # print "\n"
    #li $v0, 4
    #la $a0, nl
    #syscall

    # si i % j == 0 -> pas premier, sinon (< 0) on continue la boucle
    beq $s3, $0, anp_end_loop_false

    # i++ (i local)
    addi $t0, $t0, 1
    b anp_loop
anp_end_loop_true:
    # ajouter i dans $s0
    add $s0, $s0, $s2
    #li $s6, 1
anp_end_loop_false:
    move $ra, $s7
    jr $ra




main:
infinite_loop:
    move $s0, $0

    # print str ask_int
    li $v0, 4
    la $a0, ask_int
    syscall

     # read int
    li $v0, 5
    syscall
    move $s1, $v0
    #li $s1, 100

    # init i à 0
    li $s2, 1
loop:
    # loop from $s2 (1) to $s1 (n)
    beq $s2, $s1, end_loop
    jal add_next_premier

    # print i
    #li $v0, 1
    #move $a0, $s2
    #syscall

    # print " "
    #li $v0, 4
    #la $a0, space
    #syscall

    # print total de la somme
    #li $v0, 1
    #move $a0, $s0
    #syscall

    # print "True" or "False" pour i premier ou non
    #beq $s6, $0, p_false
    #la $a0, t_true
    #b mini_jump
#p_false:
    #la $a0, t_false
    #b mini_jump
#mini_jump:
    #li $s6, 0
    #li $v0, 4
    #syscall

    # i++
    addi $s2, $s2, 1
    b loop
end_loop:
    # print str text_resultat_1
    li $v0, 4
    la $a0, text_resultat_1
    syscall

    # print int $s1
    li $v0, 1
    move $a0, $s1
    syscall

    # print str text_resultat_2
    li $v0, 4
    la $a0, text_resultat_2
    syscall

    # #print int $s0
    li $v0, 1
    move $a0, $s0
    syscall

    # print str nl
    li $v0, 4
    la $a0, nl
    syscall

    #j infinite_loop

    # exit
    li $v0, 10
    syscall



.data
ask_int: .asciiz "Donner un entier:\n>"
text_resultat_1: .asciiz "Somme des nombres premiers dans les "
text_resultat_2: .asciiz " premiers entiers = "
nl: .asciiz "\n"
space: .asciiz " "
t_true: .asciiz " True\n"
t_false: .asciiz " False\n"
aled: .asciiz "aled\n"
