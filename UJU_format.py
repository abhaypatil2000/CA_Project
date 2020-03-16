mnemonic = {
		'lui' : {'opcode' : '0110111'},#U format
		'auipc' : {'opcode' : '0010111'},#UJ format
		'jal' : {'opcode' : '1101111'}
		}

def UJU_Format(instruction):#check for negative numbers
	instruction = instruction.replace(" ", ",")
	ins = instruction.split(",")
	while "" in ins:
		ins.remove("")
	opc = ins[0]#mnemonic
	op = ins[0]#done
	rd = ins[1]#done

	imm_temp = ins[2]#before the rearrangment or splicing
	imm_final = ''#after rearrangement
	op = str(mnemonic[op]['opcode'])
	rd = str(bin(int(rd.replace('x', '')))).replace('0b', '').rjust(5, '0')
	imm_temp = str(bin(int(imm_temp, 0))).replace('0b', '').rjust(32, '0')[11:32]##now we have 21 bits from lsb excl

	if (opc == 'jal'):#exclude the imm[21]
		imm_final = imm_temp[0:20]# + imm_temp[10:20] + imm_temp[9] + imm_temp[1:9]
	else:#if lui or addi
		imm_final = imm_temp[1:21]

	machine_code = imm_final + rd + op

	#print(machine_code)
	return machine_code
#	print(opc, op, rd, imm_temp, imm_final)

print(UJU_Format("jal x3, 12"))
