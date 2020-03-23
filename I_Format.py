import re
from UJU_format import UJU_Format

mnemonic_I = {
    'addi': {'opcode': '0010011', 'funct3': '000', 'type': 'value', 'label': False},
    'andi': {'opcode': '0010011', 'funct3': '111', 'type': 'value', 'label': False},
    'ori': {'opcode': '0010011', 'funct3': '110', 'type': 'value', 'label': False},
    'lb': {'opcode': '0000011', 'funct3': '000', 'type': 'offset', 'label': True},
    'ld': {'opcode': '0000011', 'funct3': '011', 'type': 'offset', 'label': True},
    'lh': {'opcode': '0000011', 'funct3': '001', 'type': 'offset', 'label': True},
    'lw': {'opcode': '0000011', 'funct3': '010', 'type': 'offset', 'label': True},
    'jalr': {'opcode': '1100111', 'funct3': '000', 'type': 'both', 'label': True}
}
#addi, andi, ori, lb, ld, lh, lw, jalr
def I_Format(instruction):
	return I_Format0(instruction, 0)

def I_Format0(instruction, x):
    instruction = instruction.replace(',', ' ')
    pattern = re.compile(r'(\w+)\s+(\w+)\s+(\-?\w+)(\s+)?(.+)?')

    matches = pattern.search(instruction)

    machine_code = []
    mnemonic = matches.group(1)
    rd = matches.group(2).replace('x', '')
    imm_neg = 0
    if matches.group(4) != None:
        rs = matches.group(3).replace('x', '')
        imm = matches.group(5)
    elif matches.group(5) == None:
        rs = rd
        addr = matches.group(3)
        UJU_Format('lui x{} {}'.format(rs, addr[0:6]))
        machine_code = I_Format0(mnemonic + ' ' + rs + ' 0(' + rs + ')', x + 1)
    else:
        rs = matches.group(5)
        rs = rs.replace('(', '')
        rs = rs.replace(')', '')
        rs = rs.replace('x', '')
        imm = matches.group(3)

    if imm[0] == '-':
        imm = imm.replace('-', '')
        imm = str(int(imm) - 1)
        imm_neg = 1


    if(len(machine_code) != 5):
        if imm_neg == 0:
            machine_code.append(bin(int(imm)).replace("0b", "").rjust(12, '0'))
        else:
            imm = bin(int(imm)).replace("0b", "").rjust(12, '0')
            for i in range(len(imm)):
                if imm[i] == '0':
                    imm = imm[:i] + '1' + imm[i+1:]
                else:
                    imm = imm[:i] + '0' + imm[i+1:]
            machine_code.append(imm)
        machine_code.append(bin(int(rs)).replace("0b", "").rjust(5, '0'))
        machine_code.append(mnemonic_I[mnemonic]['funct3'])
        machine_code.append(bin(int(rd)).replace("0b", "").rjust(5, '0'))
        machine_code.append(mnemonic_I[mnemonic]['opcode'])

    if (x == 0):
        machine_hex="{:08x}".format(int(''.join(machine_code),2))
        return "0x"+machine_hex
    return machine_code





print(I_Format("addi x2 x3 -3"))
