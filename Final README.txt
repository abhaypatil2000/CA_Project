TEAM NAME: APOCALYPTIC REDEMPTION

MEMBERS:

	1. Abhaysinh Sunil Patil       :	2018CSB1063
	2. Gurpreet Singh              :	2018CSB1092
	3. Kanniganti Nagasrikar       :	2018CSB1098
	4. Sarvesh Shirirsh Vhaval     :	2018CSB1121
	5. Navneet Kumar               :	2018CSB1237
	

A RISC V simulator which supports the following instruction:

	R format - add, and, or, sll, slt, sra, srl, sub, xor, mul, div, rem
	I format - addi, andi, ori, lb, ld, lh, lw, jalr
	S format - sb, sw, sd, sh
	SB format - beq, bne, bge, blt
	U format - auipc, lui
	UJ format - jal

HOW TO RUN:




GUIDLINES ON OPERATION (PRECAUTIONS):

Assembler Directives:
1. The call for assembler directives must be in lowercase. Uppercase will give an error.
eg. .Byte or .BYTE will give an error.

2. A signed value should be given. For unsigned values error will be thrown.
eg. for .byte (8bits) value from -128 to 127 (both incusive) will be supported. Same for .half, .word and .dword

3. .asciiz will take strings starting and terminating with " or '. Multiple strings can be given by separating them with <space> or <comma>
eg. .asciiz "hello" 'helo' and .asciiz 'hello',"helo" both will work

4. Assembler directives support only decimal numbers.


Parser:




Execution:




INDIVIDUAL CONTRIBUTION
Abhay : UJ_Format, U_Format, Assembler Directives, Main.py
Gurpreet : S_Format, Main.py, error handling in SB_Format
Nagasrikar :
Sarvesh :
Navneet : R_Format, phase2, main3.py
