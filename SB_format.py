# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 23:48:03 2020

@author: SARVESH
"""

isa={
     'beq' :{'opcode':'1100011', 'fun3':'000'},
     'bne' :{'opcode':'1100011', 'fun3':'001'},
     'blt' :{'opcode':'1100011', 'fun3':'100'},
     'bge' :{'opcode':'1100011', 'fun3':'101'}
     }

def SB_format(instruction):
    instruction=instruction.replace(" ",",")
    instruction_arr=instruction.split(",")
    
    while "" in instruction_arr:
        instruction_arr.remove("")
        
    machine_code=[]
    immediate=bin(int(instruction_arr[3])).replace("0b","").rjust(12,'0')
    immediate_rev=immediate[::-1]
    
    instruction_arr[1]=instruction_arr[1].replace('x','')
    instruction_arr[2]=instruction_arr[2].replace('x','')
    
    machine_code.append(immediate_rev[11])
    machine_code.append(immediate_rev[4:10])
    machine_code.append(bin(int(instruction_arr[2])).replace("0b", "").rjust(5, '0'))
    machine_code.append(bin(int(instruction_arr[1])).replace("0b", "").rjust(5, '0'))
    machine_code.append(isa[instruction_arr[0]]['fun3'])
    machine_code.append(immediate_rev[0:4])
    machine_code.append(immediate_rev[10])
    machine_code.append(isa[instruction_arr[0]]['opcode'])
    while "" in machine_code:
        machine_code.remove("")
        
    machine_bin=machine_code[0]+machine_code[1]+machine_code[2]+machine_code[3]+machine_code[4]+machine_code[5]+machine_code[6]+machine_code[7]
    machine_hex="{:08x}".format((int(machine_bin,2)))
    return "0x" + machine_hex
    
print(SB_format("bne x1,x2,4"))