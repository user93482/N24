with open('./input.txt', 'r') as f:
    input = f.read()

ingrdients = {'#':0,'.':0,'S':0,'G':0}
mazes = {}

def solver(start,maze):
    newstart = []
    i = 0
    while i < 100:
        
        for j in start:
            for k in range(len(maze)):
                for l in range(len(maze[k])):
                    if abs(k-j[0])+abs(l-j[1])== 1:
                        
                        if maze[k][l] == 'S':
                            return waymaker([k,l],maze,i)
                        elif maze[k][l] == '.':
                            maze[k][l] = i
                            newstart.append([k,l])
        start = newstart[::]
        i += 1

def waymaker(start,maze,steps):
    output = ''
    ways = {'U':[-1,0],'L':[0,-1],'R':[0,1],'D':[1,0]}
    while steps >= 0:
        for k in ways:
            if steps == 0 and maze[start[0]+ways[k][0]][start[1]+ways[k][1]] == 'G':
                output += k
                return output
            
            elif maze[start[0]+ways[k][0]][start[1]+ways[k][1]] == steps-1:
                start = [start[0]+ways[k][0],start[1]+ways[k][1]]
                steps -= 1
                output += k


temp = []
key = ''

for i in input: 
    
    if i =='\n':
        j = 0
        for i in temp:
            if i in ingrdients:
                j += 1
        
        if j == len(temp) and j != 0:
            mazes[key].append(temp)
        elif temp != []:
            key = temp[0]
            mazes[key] = []
        temp = []
    elif i != ' ':
        temp.append(i)
mazes[key].append(temp)

for i in mazes:
    
    for j in range(len(mazes[i])):
        for k in range(len(mazes[i][j])):
            if mazes[i][j][k] == 'G':
                print(f'{i}\nS',end=' ')
                for l in solver([[j,k]],mazes[i]):
                    print(l,end=' ')
                print('G\n')
