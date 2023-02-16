"""
* * * * * 
*
*
*
* * * * * * * * * * 
*
*
*
*
*
*
* * * * * * * * * * * * * * * 

"""
n = 3
u = 5
for i in range(1, n+1, 1):
    for j in range(1, i*5+1, 1):
        print("*", end="")
    print("")
    if n == i:
        break
    for k in range(1, i*3+1, 1):
        print("*")
