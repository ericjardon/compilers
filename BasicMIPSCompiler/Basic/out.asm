.data
	a:	.word 5
	b:	.word 6
.text
	li $v0 1
	li $a0 193
	syscall  
	li $t1 6
	li $t2 2
	mul $t0,6 2
	li $t1 5
	li $t2 12
	addu $t0,5 12
	la $a0 c
	li $a1 $t0
	sw $a1 0($a0)
	li $v0 1
	li $a0 17
	syscall  
	li $t1 1
	li $t2 2
	addu $t0,1 2
	li $t1 3
	li $t2 3
	mul $t0,3 3
	li $v0 1
	li $a0 9
	syscall  
