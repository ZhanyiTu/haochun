import numpy as np
def updateR():
    n = N-1
    if i == 0:
        if R[i,t] == 0:
            if R[n,t] == 1:
                R[i,t+1] = 1
            else:
                R[i,t+1] = 0
        elif R[i,t] == 1:
            if R[i+1,t] == 0:
                R[i,t+1] = 0
            else:
                R[i,t+1] = 1
                
    elif i > 0 and i < n:
        if R[i,t] == 0:
            if R[i-1,t] == 1:
                R[i,t+1] = 1
            else:
                R[i,t+1] = 0
        elif R[i,t] == 1:
            if R[i+1,t] == 0:
                R[i,t+1] = 0
            else:
                R[i,t+1] = 1
                
    elif i == n:
        if R[i,t] == 0:
            if R[i-1,t] == 1:
                R[i,t+1] = 1
            else:
                R[i,t+1] = 0
        elif R[i,t] == 1:
            if R[0,t] == 0:
                R[i,t+1] = 0
            else:
                R[i,t+1] = 1
    
    return R[i,t+1]

N = 9
T = 3
R = np.zeros(shape = (N,T+1))
R[:,0] = [1,0,0,1,1,1,0,0,1]
for t in range(T):
    for i in range(N):
        updateR()


N = 9
T = 3
M = 5
#r = np.zeros(shape = (N,T+1))
#r[:,0] = [1,0,0,1,1,1,0,0,1]

Traj = np.zeros(shape = (M,T+1))
Traj[:,0] = [1,4,5,6,9]


def new_position():
    r=R[:,t]                    
    for a in Traj[:,t]:
        
            b = int(a%9)
            if r[b] == 0:
                Traj[i,t+1] = Traj[i,t] + 1
            else:
                Traj[i,t+1] = Traj[i,t]
    return Traj[i,t+1]

for t in range(T):
    for i in range(M):
        new_position()
print(Traj)