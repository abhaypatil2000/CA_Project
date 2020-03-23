mnemonic = {
  
    'sb': {'opcode': '0100011', 'funct3': '000'},
    'sh': {'opcode': '0100011', 'funct3': '001'},
    'sw': {'opcode': '0100011', 'funct3': '010'},
    'sd': {'opcode': '0100011', 'funct3': '011'},
}

def S_Format(instruction):
    instruction = instruction.replace(')', '')
    instruction = instruction.replace('(', ',')
    instruction = instruction.replace(' ', ',')
    instruction_arr = instruction.split(',')
    while '' in instruction_arr:
        instruction_arr.remove('')
    (instruction_arr[2], instruction_arr[3]) = (instruction_arr[3], instruction_arr[2])
    machine_code = []
    if int(instruction_arr[3]) < 2**12:
        immediate=bin(int(instruction_arr[3])).replace("0b","").rjust(12,'0')
        imm1=str(immediate)[0:7]
        imm2= str(immediate)[7:12]
        machine_code.append(imm1)
    else:
        print("Immediate value too large. Must be less than " + str(2**12))

    instruction_arr[1] = instruction_arr[1].replace('x', '')
    instruction_arr[2] = instruction_arr[2].replace('x', '')
    machine_code.append(bin(int(instruction_arr[1])).replace("0b", "").rjust(5, '0'))
    machine_code.append(bin(int(instruction_arr[2])).replace("0b", "").rjust(5, '0'))
    machine_code.append(mnemonic[instruction_arr[0]]['funct3'])
    machine_code.append(imm2)
    machine_code.append(mnemonic[instruction_arr[0]]['opcode'])
    machine_hex="{:08x}".format(int(''.join(machine_code),2))
    return "0x"+machine_hex

print(SFormat("sb x1, 10(x2)"))
