

#Exo 0
#   3. Le prog tente d'aller au label "main", mais ne peut pas, car il n'existe pas (aucun fichier n'a été chargé)
#   5. Visuellement, il ne se passe rien (concrètement, mains est bien appelé, mais la seul instruction qu'il contient et de revenir à l'adresse de la fonction appelante (donc hors du main.s, je crois)
#   6. Bah rien wtf
#   7. a. On ne dit que le label "main" existe déjà (car main.s est tjr chargé, il faut réinitialiser d'abord, avec "reinit")
#   8. ligne...
        5: je ne sais pas
        6: charge 42 dans le registre $t0
        7:   --      9    --             $t1
        8: met la somme des registres $t0 et $t1 dans $t2
        9: déplace le contenu de $t0 dans $a0
       10: on charge 1 dans $v0
       11: syscall execute une certain manip en fonction de se que contient $v0 (dans ce cas si, $v0 contient 1, ce qui fait un print)
       12: jump vers l'adresse dans $ra ("fonction" appelante de main)
       ... des bails hors de "basic.s"
        



#Exo 1
#   1. Fait
#   2. Il semblerait que syscall 5 stock la valeur dans $v0 (c'est dans le cours, et ça se comprends dans le programme (avec move $t0 $v0, alors qu'en théorie, on écrit dans $v0)
#   3. on est bloqué dans le prog
#   4. ça boucle dans main (à cause de $ra qui est écrasé lors du jump vers "add_user_num", mais de retour dans "main", $ra ne correspond plus à l'"appellant" de main, mais à "main" lui même)
#   5. technique de shlagos. avant de jump vers "add_user_num", on stocke $ra (dans $s7 par exemple), en après le jump, on rétabli $ra (qui est dans $s7)
#   6. Problème. Si on écrase $s7 dans "add_user_num", bah on est niqué mdr
#   7. une pile (pas mon idée, mais une bonne idée), mais je vois pas comment (avec les 32 registres) faire cette pile





.text
.globl main



main:





.data

