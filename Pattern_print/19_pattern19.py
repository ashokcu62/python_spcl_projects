"""


X 
X X 
_ X X 
X X 
X X 
_ _ X X X X 
X X 
X X 
X X 
_ _ _ X X X X X X X X 

"""
n = 3
for i in range(1, n+1, 1):
    for a in range(1, i+1, 1):
        for f in range(1,2+1,1):
                
            print("X", end="")
        print("")
    
    for c in range(1, i+1, 1):
        print("_", end="")
    for d in range(1, 2*i+1, 1):
        print("X", end="")
    print("")
