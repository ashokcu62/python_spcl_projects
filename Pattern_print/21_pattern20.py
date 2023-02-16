"""
X X X X 
X X X 
X
X
X X X 
X X 
X
X
X X 
X

"""
n = 4
for i in range(1, 3+1, 1):
    for j in range(i,n+1,1):
        print("X",end="")
    print("")
    for k in range(i,n,1):
        print("X",end="")
    print("")
    if i==3:
        break
    for l in range(1,2+1,1):
        print("X")

    
