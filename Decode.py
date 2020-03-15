reg_file = {
		'x0' : 0, 'x1' : 0, 'x2' : 0x7ffffffc, 'x3' : 0,
		'x4' : 0, 'x5' : 0, 'x6' : 0, 'x7' : 0,
		'x8' : 0, 'x9' : 0, 'x10' : 0, 'x11' : 0,
		'x12' : 0, 'x13' : 0, 'x14' : 0, 'x15' : 0,
		'x16' : 0, 'x17' : 0, 'x18' : 18, 'x19' : 0,
		'x20' : 0, 'x21' : 0, 'x22' : 0, 'x23' : 0,
		'x24' : 0, 'x25' : 0, 'x26' : 0, 'x27' : 27,
		'x28' : 0, 'x29' : 0, 'x30' : 0, 'x31' : 31,
		}

#RA is the first operand of the ALU
#RB is the second operand of the ALU
#tempdrd contains the register to which we will write

prog_ptr = 123

def Decode(x):#x is a string
	decode_op = x[25:32]#op is the opcode
	R_dop = ['0110011']#decode opcode
	I_dop = ['0010011', '0000011', '1100111']
	S_dop = ['0100011']
	SB_dop = ['1100011']
	UJU_dop = ['0110111', '0010111', '1101111']
	if (decode_op in R_dop):
		tempdr1 = 'x' + str(int(x[12:17], 2))
		tempdr2 = 'x' + str(int(x[7:12], 2))
		tempdrd = 'x' + str(int(x[20:25], 2))
		
		#these temp contain the register not the register content
		#print(tempdr1, tempdr2, tempdrd)
		RA = reg_file[tempdr1]
		RB = reg_file[tempdr2]
		
	elif (decode_op in I_dop):
		tempdr1 = 'x' + str(int(x[12:17], 2))
		tempdrd = 'x' + str(int(x[20:25], 2))
		
		RA = reg_file[tempdr1]
		RB = int(x[0:12], 2)

	elif (decode_op in S_dop):
		tempdr1 = 'x' + str(int(x[12:17], 2))
		tempdr2 = 'x' + str(int(x[7:12], 2))
		imm_S_op = x[0:7] + x[20:25]
		
		RA = reg_file[tempdr1]
		RB = int(imm_S_op, 2)
		RM = reg_file[tempdr2]
		
	elif (decode_op in SB_dop):
		tempdr1 = 'x' + str(int(x[12:17], 2))
		tempdr2 = 'x' + str(int(x[7:12], 2))
		imm_SB_op = x[0:7] + x[20:25]
		
		RA = reg_file[tempdr1]
		RB = reg_file[tempdr2]
		IMM_OFFSET = 2 * int(imm_SB_op, 2) # add this to pc later
		
	elif (decode_op in UJU_dop):
		tempdrd = 'x' + str(int(x[20:25], 2))
		if (decode_op == '0110111'): # lui
			RB = int(x[0:20].ljust(32, '0'), 2)
			RA = 0
		elif (decode_op == '0010111'): # auipc
			RB = int(x[0:20].ljust(32, '0'), 2)
			RA = prog_ptr
		elif (decode_op == '1101111'): # jal
			RB = 2 * int(x[0:20], 2)
			#RB = int((x[0] + x[12:20] + x[11] + x[1:11]).ljust(32, '0'), 2)
			RA = prog_ptr
		
#in the end do reg_file[tempdrd] = RY


Decode('00000000000000000110000111101111') #jal x3, 12












