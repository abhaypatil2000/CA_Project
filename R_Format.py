import re
# class IncorrectArgumentError(Error):
#     pass
def R_Format(input):
    mnemonics = {'add':['0110011','000','0000000'],'and':['0110011','111','0000000'],'or':['0110011','110','0000000'], 'sll':['0110011','001','0000000'],'slt':['0110011','010','0000000'],'sra':['0110011','101','0100000'],'srl':['0110011','101','0000000'],'sub':['0110011','000','0100000'],'xor':['0110011','100','0000000'],'mul':['0110011','000','0000001'],'div':['0110011','100','0000001'],'rem':['0110011','110','0000001']}
    input = (input.split('#'))[0]
    x = re.compile(r'^\s*(?P<mnemonic>\w+)\s+x(?P<rd>[0-31])\s*,\s*x(?P<rs1>[0-31])\s*,\s*x(?P<rs2>[0-31])\s*$')
    if x.search(input) == None:
        return ''
    else:
        y = x.search(input)
        if y.group('mnemonic') not in mnemonics.keys():
            return ''
        else:
            z = mnemonics[y.group('mnemonic')]
            opcode = z[0]
            func3 = z[1]
            func7 = z[2]
            rd = "{:05b}".format(int(y.group('rd')))
            rs1 = "{:05b}".format(int(y.group('rs1')))
            rs2 = "{:05b}".format(int(y.group('rs2')))
            machine_hex='0x'+"{:08x}".format(int(func7 + rs2 + rs1 + func3 + rd + opcode,2))
            print (machine_hex)
            return machine_hex
        
print (R_Format("add,x1,x2,x3"))