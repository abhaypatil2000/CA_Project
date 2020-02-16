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

def to_IFormat(instruction):
    instruction = instruction.replace(',', ' ')
    pattern = re.compile(r'(\w+)\s+(\w+)\s+(\w+)(\s+)?(.+)?')
    matches = pattern.search(instruction)
    print(matches)
    machine_code = []
    mnemonic = matches.group(1)
    rd = matches.group(2).replace('x', '')

    for i in range(6):
        print(matches.group(i))

    if matches.group(4) != None:
        rs = matches.group(3).replace('x', '')
        imm = matches.group(5)
    elif matches.group(5) == None:
        rs = rd
        addr = hex(int(matches.group(3)))
        print(UJU_Format('lui {} 0x{}'.format(rs, addr[-5:])))
        print(to_IFormat(mnemonic + ' ' + rs + ' 0(' + rs + ')' ))
    else:
        rs = rs.replace('(', '')
        rs = rs.replace(')', '')

    machine_code.append(mnemonic_I[mnemonic]['opcode'])
    machine_code.append(bin(int(rd)).replace("0b", "").rjust(5, '0'))
    machine_code.append(bin(int(rs)).replace("0b", "").rjust(5, '0'))
    machine_code.append(bin(int(imm)).replace("0b", "").rjust(12, '0'))
    print(machine_code)
    return machine_code
    # if int(instruction_arr[3]) < 2**12:
    #     machine_code.append(bin(int(instruction_arr[3])).replace("0b", "").rjust(12, '0'))
    # else:
    #     print("Immediate value too large. Must be less than " + str(2**12))
    #
    # instruction_arr[1] = instruction_arr[1].replace('x', '')
    # instruction_arr[2] = instruction_arr[2].replace('x', '')
    # machine_code.append(bin(int(instruction_arr[2])).replace("0b", "").rjust(5, '0'))
    # machine_code.append(mnemonic[instruction_arr[0]]['funct3'])
    # machine_code.append(bin(int(instruction_arr[1])).replace("0b", "").rjust(5, '0'))
    # machine_code.append(mnemonic[instruction_arr[0]]['opcode'])
    # print(machine_code)

to_IFormat("addi x1, x2, 300")
# to_IFormat("lb x1, 10(x2)")
to_IFormat("lb x1, 0x50000000")
