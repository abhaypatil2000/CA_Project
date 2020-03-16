from UJU_format import *
from I_Format import *
from R_Format import *
from SB_format import *
from S_Format import *
from common_backend import *
from Parser import parse

def main1():
	file_read = open("input.txt","r")
	file_write = open("output.mc","w")
	lines =file_read.readlines()
	print(lines)
	lines=[val for val in lines if val!='\n']
	lines2 = []
	for line in lines:
		line2=line.replace('\n',' ')
		lines2.append(line2)
	lines = lines2.copy()
	print(lines)
	for i in range(len(lines)):
		parse(lines[i], i+1)
	file_write.writelines(lines)
	file_read.close()
	file_write.close()

# def main1():
# 	file_read = open("input.txt", "r")
# 	file_write = open("output.txt", "w")
# 	lines = file_read.readlines()
# 	for line in lines:
# 		parse(line)
#
# 	print(x)
# 	file_write.writelines(x)
# 	file_read.close()
# 	file_write.close()
#


def main2():
	fetch(prog_ptr)
	decode()
	execute()
	memaccess()
	update()



main1()
