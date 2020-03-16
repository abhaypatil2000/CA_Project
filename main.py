from UJU_Format import *
from I_Format import *
from common_backend import *
from Parser import parse

def main1():
	file_read = open("input.txt", "r")
	file_write = open("output.txt", "w")
	lines = file_read.readlines()
	for line in lines:
		parse(line)

	print(x)
	file_write.writelines(x)
	file_read.close()
	file_write.close()



def main2():
	fetch(prog_ptr)
	decode()
	execute()
	memaccess()
	update()



main1()
