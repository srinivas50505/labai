import copy
def print_puzzle(puzzle):
    for row in puzzle:
        print(row)
    print()
def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j]==0:
                return i,j
def h(puzzle,goal):
    res=0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j]!=goal[i][j]:
                res=res+1
    return res
def hill_climbing(intial,goal):
    current=copy.deepcopy(intial)
    
    while True:
        i_jblank=find_blank(current)
        if i_jblank is  None:
                break
        i,j=i_jblank
        neighbours=[]
        if i>0:
            temp=copy.deepcopy(current)
            temp[i][j]=temp[i-1][j]
            temp[i-1][j]=0
            neighbours.append(temp)
        if i<2:
            temp=copy.deepcopy(current)
            temp[i][j]=temp[i+1][j]
            temp[i+1][j]=0
            neighbours.append(temp)
        if j>0:
            temp=copy.deepcopy(current)
            temp[i][j]=temp[i][j-1]
            temp[i][j-1]=0
            neighbours.append(temp)
        if j<2:
            temp=copy.deepcopy(current)
            temp[i][j]=temp[i][j+1]
            temp[i][j+1]=0
            neighbours.append(temp)
        if not neighbours:
            break
        neighbours.sort(key=lambda x: h(x, goal))
        next_move = neighbours[0]
        if h(next_move, goal) >= h(current, goal):
            break
        current = next_move
    return current
    

intial_state=[[1,2,3],[5,6,0],[7,8,4]]
goal_state=[[1,2,3],[5,8,6],[0,7,4]]
print("intial_state")
print_puzzle(intial_state)
print("goal_state")
print_puzzle(goal_state)
solution=hill_climbing(intial_state,goal_state)
print("solution")
print_puzzle(solution)
