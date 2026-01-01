n = 6
alpha = [
    "A","B","C","D","E","F","G","H","I","J",
    "K","L","M","N","O","P","Q","R","S","T",
    "U","V","W","X","Y","Z"
]
a = 0


for i in range(n):
    print((n-i) * " ", end="")
    
    for j in range(i):
        if a > 25 or a < 0:
            a = 0
        print(alpha[a], end="")
        a+=1
        
    for j in range(i, -1, -1):
        if a > 25 or a < 0:
            a = 0
        print(alpha[a], end="")
        a+=1
    
    print("")
    
    
    
    
    
    
# for i in range(n): # 0, 1, 2, 3, 4, 5
#     print((n-i) * " ", end="") # 6, 5, 4, 3, 2, 1
    
#     for j in range(i): # 
#         print("*", end="")

#     for j in range(i-1): # 
#         print("*", end="")
        
#     print("")

# for i in range(n,-1,-1): # 0, 1, 2, 3, 4, 5
#     print((n-i) * " ", end="") # 6, 5, 4, 3, 2, 1
    
#     for j in range(i): # 
#         print("*", end="")

#     for j in range(i-1): # 
#         print("*", end="")
        
#     print("")