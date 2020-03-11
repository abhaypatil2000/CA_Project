from UJU_Format import *
from I_Format import *


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
	
	
main()