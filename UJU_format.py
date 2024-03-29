import re
mnemonic = {
		'lui' : {'opcode' : '0110111'},#U format
		'auipc' : {'opcode' : '0010111'},#UJ format
		'jal' : {'opcode' : '1101111'}
		}

class SntxErr(Exception):
	pass

class BigData(Exception):
	pass

def UJU_Format(instruction):#check for negative numbers
	instruction = instruction.replace(" ", ",")
	ins = instruction.split(",")
	while "" in ins:
		ins.remove("")
	if (len(ins) != 3):
		raise SntxErr("Wrong number of arguments")
	opc = ins[0]#mnemonic
	op = ins[0]#done
	rd = ins[1]#done
	if (rd[0] != 'x'):
		raise SntxErr("No destination register given")
	

	imm_temp = ins[2]#before the rearrangment or splicing
	imm_final = ''#after rearrangement
	
	for ch in imm_temp:
		if (ch not in ['0','1','2','3','4','5','6','7','8','9']):
			raise SntxErr("Not a decimal number")
	if int(imm_temp) >= 2**19 or int(imm_temp) < -(2**19):
        	raise MyException("Immediate value out of bounds!")
	op = str(mnemonic[op]['opcode'])
	rd = str(bin(int(rd.replace('x', '')))).replace('0b', '').rjust(5, '0')
	imm_temp = str(bin(int(imm_temp, 0))).replace('0b', '').rjust(32, '0')[11:32]##now we have 21 bits from lsb excl

	if (opc == 'jal'):#exclude the imm[21]
		imm_final = imm_temp[0] + imm_temp[10:20] + imm_temp[9] + imm_temp[1:9]
		#imm_final = imm_temp[0:20]# + imm_temp[10:20] + imm_temp[9] + imm_temp[1:9]
	else:#if lui or auipc
		imm_final = imm_temp[1:21]

	machine_code = imm_final + rd + op
	machine_hex="{:08x}".format((int(machine_code,2)))
	return "0x"+machine_hex
#	print(opc, op, rd, imm_temp, imm_final)

#print(UJU_Format("jal x3, 12"))
