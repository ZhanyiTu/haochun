def update(R, i, t):
    if i == 0:
        if R[i][t] == 0:
            if R[8][t] == 1:
                R[i].append(1)
            else:
                R[i].append(0)
        elif R[i][t] == 1:
            if R[8][t] == 0 and R[i+1][t] == 0:
                R[i].append(0)
            else:
                R[i].append(1)
    elif i > 0 and i < 8:
        if R[i][t] == 0:
            if R[i-1][t] == 1:
                R[i].append(1)
            else:
                R[i].append(0)
    
        elif R[i][t] == 1:
            if R[i-1][t] == 0 and R[i+1][t] == 0:
                R[i].append(0)
            else:
                R[i].append(1)
    elif i == 8:
        if R[i][t] == 0:
            if R[i-1][t] == 1:
                R[i].append(1)
            else:
                R[i].append(0)
    
        elif R[i][t] == 1:
            if R[i-1][t] == 0 and R[0][t] == 0:
                R[i].append(0)
            else:
                R[i].append(1)
R = [[] for i in range(9)]
R[0].append(1)
R[1].append(0)
R[2].append(0)
R[3].append(1)
R[4].append(1)
R[5].append(1)
R[6].append(0)
R[7].append(0)
R[8].append(1)
for i in range(9):
    for j in range(1):
        update(R, i, j)
for i in range(9):
    for j in range(len(R[i])):
        print(R[i][j], end='')
    print()

'''
    "1 & 0 & 1 & 0\\\\\n",
    "0 & 1 & 0 & 1\\\\\n",
    "0 & 0 & 1 & 1\\\\\n",
    "1 & 1 & 1 & 0\\\\\n",
    "1 & 1 & 0 & 1\\\\\n",
    "1 & 0 & 1 & 0\\\\\n",
    "0 & 1 & 0 & 1\\\\\n",
    "0 & 0 & 1 & 0\\\\\n",
    "1 & 1 & 0 & 1\\\\\n",
'''
