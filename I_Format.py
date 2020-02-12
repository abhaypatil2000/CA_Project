mnemonic = {
    'addi': {'opcode': '0010011', 'funct3': '000'},
    'andi': {'opcode': '0010011', 'funct3': '111'},
    'ori': {'opcode': '0010011', 'funct3': '110'},
    'lb': {'opcode': '0000011', 'funct3': '000'},
    'ld': {'opcode': '0000011', 'funct3': '011'},
    'lh': {'opcode': '0000011', 'funct3': '001'},
    'lw': {'opcode': '0000011', 'funct3': '010'},
    'jalr': {'opcode': '1100111', 'funct3': '000'}
}
#addi, andi, ori, lb, ld, lh, lw, jalr



def to_IFormat(instruction):
    number_of_commas = instruction.count(",")
    if number_of_commas == 1:
        instruction = instruction.replace(')', '')
        instruction = instruction.replace('(', ',')
    instruction = instruction.replace(' ', ',')
    instruction_arr = instruction.split(',')
    while '' in instruction_arr:
        instruction_arr.remove('')
    if number_of_commas == 1:
        (instruction_arr[2], instruction_arr[3]) = (instruction_arr[3], instruction_arr[2])

    machine_code = []
    if int(instruction_arr[3]) < 2**12:
        machine_code.append(bin(int(instruction_arr[3])).replace("0b", "").rjust(12, '0'))
    else:
        print("Immediate value too large. Must be less than " + str(2**12))

    instruction_arr[1] = instruction_arr[1].replace('x', '')
    instruction_arr[2] = instruction_arr[2].replace('x', '')
    machine_code.append(bin(int(instruction_arr[2])).replace("0b", "").rjust(5, '0'))
    machine_code.append(mnemonic[instruction_arr[0]]['funct3'])
    machine_code.append(bin(int(instruction_arr[1])).replace("0b", "").rjust(5, '0'))
    machine_code.append(mnemonic[instruction_arr[0]]['opcode'])
    print(machine_code)

to_IFormat("addi x1, x2, 300")
to_IFormat("lb x1, 10(x2)")
