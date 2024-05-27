with open('./input.txt', 'r') as f:
    input = f.read()

def MatrixMult(A,B):
	output = []
	for i in range(len(A)):
		output.append([])
		for j in range(len(B[0])):	
			output[i].append(0)
			k = 0
			while k < len(B):
				output[i][j] += int(A[i][k])*int(B[k][j])
				k += 1
    
	return output

def MatrixSum(matrices):
    output = []
    i = 0
    for i in range(len(matrices[0])):
        output.append([])
        for j in range(len(matrices[0][0])):
            output[i].append(0)
    
    for i in range(len(matrices)):
        for j in range(len(matrices[i])):
            for k in range(len(matrices[i][j])):
                output[j][k] += int(matrices[i][j][k])
        
    return output

lines = []
matrices = {}
temp = ''
key = ''
j = 0

for i in input: 
    if i == '\n': 
        if temp != '':
            lines.append(temp)
        temp = ''
    else:
        temp += i
lines.append(temp)

i = 1
key = ''
while i < len(lines):
    if lines[i] == 'operations':
        i += 1
        break
    temp = lines[i].split()
    if len(temp) == 1:
        key = temp[0]
        matrices[key] = []
    else:
        matrices[key].append(temp)
    i += 1

while i < len(lines):
    operands = []
    operators = []
    newops = []
    keys = []
    
    for j in range(len(lines[i])):
        if lines[i][j] in matrices.keys():
            keys.append(lines[i][j])
            operands.append(matrices[keys[-1]])
        
        elif lines[i][j] != ' ':
            operators.append(lines[i][j])
    
    k = 0
    while k < len(operators):
        if operators[k] == '*':
            
            operands[k+1] = MatrixMult(operands[k],operands[k+1])
            operands.pop(k)
        
        newops.append(operators.pop(k))
    
    for j in range(len(keys)-1):
        print(keys[j],newops[j],end=' ')
    print(keys[-1])
    
    temp = MatrixSum(operands)
    for j in temp:
        for k in j:
            print(k,end=' ')
        print()
    print()
    
    i += 1
    
