from UJU_Format import *
from I_Format import *

reg_file = {
		'x0' : 0, 'x1' : 0, 'x2' : 0x7ffffffc, 'x3' : 0,
		'x4' : 0, 'x5' : 0, 'x6' : 0, 'x7' : 0,
		'x8' : 0, 'x9' : 0, 'x10' : 0, 'x11' : 0,
		'x12' : 0, 'x13' : 0, 'x14' : 0, 'x15' : 0,
		'x16' : 0, 'x17' : 0, 'x18' : 0, 'x19' : 0,
		'x20' : 0, 'x21' : 0, 'x22' : 0, 'x23' : 0,
		'x24' : 0, 'x25' : 0, 'x26' : 0, 'x27' : 0,
		'x28' : 0, 'x29' : 0, 'x30' : 0, 'x31' : 0,
		}

data_ptr = 0x10000000
text_ptr = 0x00000000
heap_ptr = 0x10007fe8
prog_ptr = 0x00000000
memory_ptrs = (data_ptr, text_ptr, heap_ptr, prog_ptr)

memory = {}

RY, RZ, RM, RA, RB = 0, 0, 0, 0, 0
temp_registers = (RA, RB, RY, RZ, RM)

temp_registers

def main1():
	file_read = open("input.txt", "r")
	file_write = open("output.txt", "w")
	x = file_read.readlines()
#	print (x)
#	for i in x:
#		file_write.write(i)
	file_write.writelines(x)
	file_read.close()
	file_write.close()
	a = UJU_Format("lui x3, 0x12AB7")
	b = I_Format("lw x2, 0x10000008")
	print(a+'\n'+b)



def main2():
	fetch(prog_ptr)
	decode()
	execute()
	memaccess()
	update()



main1()
