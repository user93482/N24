abc = "abcdefghijklmnopqrstuvwxyz"
nums = '0123456789'

with open('./input.txt', 'r') as f:
    input = f.read()

input = input.lower()
candidates = ['']

j = 0
for i in input: #szétszedi soronként, és eltávolitja a felesleges karaktereket
    if i =='\n':
        candidates.append('')
        j+=1
    elif i in abc or i in nums:
        candidates[j] += i

palindromes = []
uniques = []
qualified = []

for i in range(len(candidates)): # végigmegy a karatkerláncokon
    j=0
    uniques.append([])
    while j < int(len(candidates[i])/2)+1: #végigmegy a karakterein
        
        if candidates[i][j] not in uniques[i]: 
            uniques[i].append(candidates[i][j])

        if candidates[i][j] != candidates[i][-j-1]:
            break
        j+=1

    if j == int(len(candidates[i])/2)+1:
        palindromes.append(candidates[i])
        qualified.append('YES')
        uniques[i] = len(uniques[i])
    else:
        qualified.append('NO')
        uniques[i] = -1

for i in range(len(qualified)):
    print(f"{qualified[i]}, {uniques[i]}")
