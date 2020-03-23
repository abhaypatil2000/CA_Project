#from common_backend import *
#use memory and data_ptr
#.byte, .half, .word, .dword, .asciiz

#
class UnknownAD(Exception):
    pass

class BigData(Exception):
	pass

dict = {}
ptr = 0
def asembler_directives():
	global ptr
	asmdirinp = open("input.txt", "r")
	inplist = asmdirinp.readlines()
	for lien in inplist:#lien is line
		if (lien[-1] == '\n'):
			lien = lien[:-1]
		if ('.' in lien):
			while (':' in lien):
				lien = lien[1:]
			lien = lien.replace(" ", ",")
			lien_list = lien.split(',')
			while ("" in lien_list):
				lien_list.remove("")
#			print(lien_list)
			if (lien_list[0] != '.data' and lien_list[0] != '.text'):
				if (lien_list[0] == '.byte'):
					lien_list.remove(lien_list[0])
					data_list = lien_list
					for data in data_list:
						if (int(data) > 0xff):
							raise BigData("data too big to fit")
						dict[ptr] = int(data)
						print(dict[ptr])
						ptr = ptr + 1
						
				elif (lien_list[0] == '.asciiz'):
					lien_list.remove(lien_list[0])
					data_list = lien_list
					for data in data_list:
						#print(data + '-------')
						for ch in data[1:-1]:
							dict[ptr] = ord(ch)
							print(ch)
							ptr = ptr + 1
					
				elif (lien_list[0] == '.half'):
					lien_list.remove(lien_list[0])
					data_list = lien_list
					
				elif (lien_list[0] == '.word'):
					lien_list.remove(lien_list[0])
					data_list = lien_list
					
				elif (lien_list[0] == '.dword'):
					lien_list.remove(lien_list[0])
					data_list = lien_list
					
				else:
					raise UnknownAD("unknown assembler directive")
					#unrecognised assembler directive
				
			
#			print(lien_list)
	
	
	return dict
	asmdirinp.close()
	
	
#asembler_directives()
