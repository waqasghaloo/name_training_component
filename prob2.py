building = [["B","B","B"],["E","E","E"],["B","B","B"]]

def dfs(building, i, j):
    
    if (i < 0) or (i>=len(building)) or (j<0) or (j>=len(building[i])) or building[i][j]!="B":
        return
    
    building[i][j]="V"
    dfs(building,i+1,j)
    dfs(building,i-1,j)
    dfs(building,i,j+1)
    dfs(building,i,j-1)


count = 0
for i in range(len(building)):
    for j in range(len(building[i])):
        if building[i][j]=="B":
            print(i,j)
            count+=1
            dfs(building, i, j)
print(count)

