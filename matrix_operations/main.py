with open('./input.txt', 'r') as f:
    input = f.read()

def MatrixMult(A,B):
	return
	

def MatrixSum(matrices):
    output = []
    
    for i in range(len(matrices[0])):
        output.append([])
        for j in range(len(matrices[i][0])):
            output[i].append(0)
    
    for i in matrices:
        for j in range(len(i)):
            
            for k in range(len(i[j])):
                
                output[j][k] += int(i[j][k])
    
        
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
    print(lines[i])
    i += 1


while i < len(lines):
    operands = []
    operators = []
    
    for j in range(len(lines[i])):
        if lines[i][j] in matrices.keys():
            operands.append(matrices[lines[i][j]])
        elif lines[i][j] != ' ':
            operators.append(lines[i][j])
    
    
    k = 0
    while k < len(operators):
        if operators[k] == '*':
            
            
            operands[k+1] = operands[k+1] #MatrixMult(0,0)
            operators.pop(k)
            operands.pop(k)
            print(operands)
        else:
            
            k += 1
    
    temp = MatrixSum(operands)
    for j in temp:
        print(j)
    print()
    i += 1
    
