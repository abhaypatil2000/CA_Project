from I_format.py import *
def main():
	file_read = open("input.txt", "r")
	file_write = open("output.txt", "w")
	x = file_read.readlines()
#	print (x)
#	for i in x:
#		file_write.write(i)
	file_write.writelines(x)
	file_read.close()
	file_write.close()
	to_IFormat("addi x1, x2, 300")
main()