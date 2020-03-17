#Control Signals
Branch = 0
MemRead = 0
MemtoReg = 0
# ALUOp = 0
MemWrite = 0
ALUSrc1 = 0
ALUSrc2 = 0
PCSrc = -1
PCReg = 0 #Signal if the PC is updated by the Register value

#Register File inputs and Outputs
RegWrite = 0
ReadData1 = 0
ReadData2 = 0
ReadRegister1 = 0
ReadRegister2 = 0
WriteRegister = 0
WriteDataRegFile = 0

#Immediate Generation
ImmGenOutput = 0

#ALU Control
ALUControl = 0

#ALUinputs
ALU_input1 = 0
ALU_input2 = 0

#PC
PC = 0

#Instruction Memory
ReadAddress = 0
Instruction = '0' * 32

#ALU output
Zero = 0
LessThan = 0
GE = 0
ALUResult = 0

#Data Memory
Address = 0
WriteData = 0
ReadData = 0

#Exit Signal
EXIT = False
#Registers
reg_file = {
		'x0' : 0, 'x1' : 0, 'x2' : 0x7ffffffc, 'x3' : 0,
		'x4' : 0, 'x5' : 0, 'x6' : 0, 'x7' : 0,
		'x8' : 0, 'x9' : 0, 'x10' : 0, 'x11' : 0,
		'x12' : 0, 'x13' : 0, 'x14' : 0, 'x15' : 0,
		'x16' : 0, 'x17' : 0, 'x18' : 0, 'x19' : 0,
		'x20' : 0, 'x21' : 0, 'x22' : 0, 'x23' : 0,
		'x24' : 0, 'x25' : 0, 'x26' : 0, 'x27' : 0,
		'x28' : 0, 'x29' : 0, 'x30' : 0, 'x31' : 0,
		}

#clock
clock = 0

#TempMem
TempMem = {}
def initialize_mem():
    global TempMem
    TempMem.clear()
    fp = open("1.mc", "r+")
    for line in fp:
        inst = line.split()
        if(len(inst) != 2):
            break
        a = int(inst[0], 16)
        b = inst[1][2:]
        if(len(b)==8):
            TempMem[a] = b[6:]
            TempMem[a+1] = b[4:6]
            TempMem[a+2] = b[2:4]
            TempMem[a+3] = b[0:2]
        elif(len(b)==4):
            TempMem[a] = b[2:]
            TempMem[a+1] = b[0:2]
        else:
            TempMem[a] = b
    fp.close()
def exit_routine():
    global TempMem
    global clock
    fp = open("1.mc", "r+")
    for i in TempMem.keys():
        fp.write(hex(i) + " " + '0x'+TempMem[i]+'\n')
    fp.close()
def reset():
    initialize_mem()
    global reg_file
    reg_file = {
		'x0' : 0, 'x1' : 0, 'x2' : 0x7ffffffc, 'x3' : 0,
		'x4' : 0, 'x5' : 0, 'x6' : 0, 'x7' : 0,
		'x8' : 0, 'x9' : 0, 'x10' : 0, 'x11' : 0,
		'x12' : 0, 'x13' : 0, 'x14' : 0, 'x15' : 0,
		'x16' : 0, 'x17' : 0, 'x18' : 0, 'x19' : 0,
		'x20' : 0, 'x21' : 0, 'x22' : 0, 'x23' : 0,
		'x24' : 0, 'x25' : 0, 'x26' : 0, 'x27' : 0,
		'x28' : 0, 'x29' : 0, 'x30' : 0, 'x31' : 0,
		}
    global clock
    clock = 0
def read_byte(address):
    global TempMem
    if address in TempMem.keys():
        return TempMem[address]
    else:
        return '00'
def read_word(address):
    return read_byte(address+3)+read_byte(address+2)+read_byte(address+1)+read_byte(address)
def read_hword(address):
    return read_byte(address+1)+read_byte(address)
def write_byte(address, data):
    global TempMem
    TempMem[address] = data
def write_word(address, data):
    write_byte(address,data[6:])
    write_byte(address+1,data[4:6])
    write_byte(address+2,data[2:4])
    write_byte(address+3,data[0:2])
def write_hword(address,data):
    write_byte(address,data[2:])
    write_byte(address+1,data[0:2])
def read_dword(address):
    return read_word(address+4) + read_word(address)
def write_dword(address, data):
    write_word(address, data[8:])
    write_word(address + 8, data[0:8])