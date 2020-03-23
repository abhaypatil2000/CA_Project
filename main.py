from UJU_format import *
from I_Format import *
from R_Format import *
from SB_format import *
from S_Format import *
from common_backend import *
from Parser import parse

class MyException(Exception):
    pass

dict = {
    'lui':{'type': 'UJU'},
    'auipc':{'type':'UJU'},
    'jal':{'type': 'UJU'},
    'sb': {'type': 'S'},
    'sh': {'type': 'S'},
    'sw': {'type': 'S'},
    'sd': {'type': 'S'},
    'addi': {'type': 'I'},
    'andi': {'type': 'I'},
    'ori': {'type': 'I'},
    'lb': {'type': 'I'},
    'ld': {'type': 'I'},
    'lh': {'type': 'I'},
    'lw': {'type': 'I'},
    'jalr': {'type': 'I'},
    'add':{'type':'R'},
    'and':{'type':'R'},
    'or':{'type':'R'}, 
    'sll':{'type':'R'},
    'slt':{'type':'R'},
    'sra':{'type':'R'},
    'srl':{'type':'R'},
    'sub':{'type':'R'},
    'xor':{'type':'R'},
    'mul':{'type':'R'},
    'div':{'type':'R'},
    'rem':{'type':'R'},
    'beq':{'type':'SB'},
    'bne':{'type':'SB'},
    'blt':{'type':'SB'},
    'bge':{'type':'SB'}
    }

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
    lines3=[]
    line_no=0
    for x in lines:
        oper= x.split()[0]
        #print (x)
        if('.' not in x and ':' not in x):
            if oper not in dict:
                 raise MyException('Error, unrecognized instruction')
            format_type=dict[oper]['type']
            #print(format_type)
            lines3.append('0x'+str(line_no))
	    line_no=line_no+4
            lines3.append(' ')
            if format_type=='S':
                y=S_Format(x)
                lines3.append(y)
            elif format_type=='R':
                y=R_Format(x)
                lines3.append(y)
            elif format_type=='I':
                y=I_Format(x)
                lines3.append(y)
            elif format_type=='SB':
                y=SB_Format(x)
                lines3.append(y) 
            elif format_type=='UJU':
                y=UJU_Format(x)
                lines3.append(y)
            else:
                raise MyException('Error, unrecognized instruction')
            lines3.append('\n')   
    file_write.writelines(lines3)
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
