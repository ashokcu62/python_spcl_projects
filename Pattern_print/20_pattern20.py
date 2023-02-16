"""
X X X X _ _
_ X X X X 
X
X X X _ _
_ X X X 
X
X
X X _ _
_ X X 
X
X
X
X _ _
_ X 
X
X
X
X


"""
n=4
for i in range(1,n+1,1):
    for j in range(i,n+1,1):
        print("X",end="")
    print("__",end="")
    print("")
    print("_",end="")
    for l in range(i,n+1,1):
        print("X",end="")
    print("")
    for m in range(1,i+1,1):
        print("X")
   