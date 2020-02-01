# CA_Project
Venus like editor for RISC V


main function reads the input line by line
1. Each line is split into 2: 
	a) the pneumonic	and
	b) the arguements
2. The pneumonic is passed into the pneumonic_dict, and the format of the pneumonic is returned. Throw an error if the pneumonic is wrong
3. Depending on the format, a differnt function is called.
4. Each format function has to check the the number of arguements and return error if required.
5. The function has another dictionary - here the pneumonic and list of number of arguments and opcode
6. The machine code in generated and returned to the main function.
