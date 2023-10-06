.text
.globl main

add_user_num:
  li $v0, 4
  la $a0, num1q
  syscall

  li $v0, 5
  syscall
  move $t0, $v0

  li $v0, 4
  la $a0, num2q
  syscall

  li $v0, 5
  syscall
  move $t1, $v0

  li $v0, 4
  la $a0, sum
  syscall

  add $a0, $t0, $t1
  li $v0, 1
  syscall

  li $v0, 4
  la $a0, nl
  syscall

  jr $ra
  
main:
  move $s7 $ra #JE SUIS PAS D'ACCORD AVEC ÇA, c'est trop schlagos
  jal add_user_num
  move $ra $s7 #JE SUIS PAS D'ACCORD AVEC ÇA, c'est trop schlagos

  jr $ra
  
  
  sub $sp, $sp, 8
  sw $ra, 4($sp)
  jal add_user_num
  lw $ra, 4($sp)

.data
num1q: .asciiz "Please enter a first number: "
num2q: .asciiz "Please enter a second number: "
sum:   .asciiz "The sum of these numbers is: "
nl:    .asciiz "\n"
