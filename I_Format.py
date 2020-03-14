import re
from UJU_Format import UJU_Format

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
    pattern = re.compile(r'(\w+)\s+(\w+)\s+(\w+)(\s+)?(.+)?')
    matches = pattern.search(instruction)
    machine_code = []
    mnemonic = matches.group(1)
    rd = matches.group(2).replace('x', '')

    # for i in range(6):
    #     print(matches.group(i))

    if matches.group(4) != None:
        rs = matches.group(3).replace('x', '')
        imm = matches.group(5)
    elif matches.group(5) == None:
        rs = rd
        addr = matches.group(3)
        UJU_Format('lui x{} {}'.format(rs, addr[0:6]))
        # print("2")
        machine_code = I_Format0(mnemonic + ' ' + rs + ' 0(' + rs + ')', x + 1)
    else:
        rs = matches.group(5)
        rs = rs.replace('(', '')
        rs = rs.replace(')', '')
        rs = rs.replace('x', '')

        imm = matches.group(3)

    if(len(machine_code) != 5):
        machine_code.append(bin(int(imm)).replace("0b", "").rjust(12, '0'))
        machine_code.append(bin(int(rs)).replace("0b", "").rjust(5, '0'))
        machine_code.append(mnemonic_I[mnemonic]['funct3'])
        machine_code.append(bin(int(rd)).replace("0b", "").rjust(5, '0'))
        machine_code.append(mnemonic_I[mnemonic]['opcode'])
     #   print(machine_code)
    if (x == 0):
        return (''.join(machine_code))
    return machine_code



#I_Format("lw x2, 0x10000008")
