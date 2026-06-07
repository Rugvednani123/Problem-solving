
'''
n = 4
for i in range(1,n+1):
    count = ""
    for j in range(1,n+1):
        count = count + " *"
    print(count)    
'''
'''
n = 5
for i in range(1,n+1):
    count = ""
    for j in range(i,n+1):
        count = count + " *"
    print(count)  
'''
'''
n = 5
for i in range(1,n+1):
    count = ""
    for j in range(1,i+1):
        count = count + " *" 
    print(count)
    '''
'''
m = 3
n = 5
for i in range(1,m+1):
    count = ""
    for j in range(1,n+1):
        count = count + " *"                 
    print(count) 
    '''
'''
n = 5
for i in range(1,n+1):
    space = ""
    for j in range(i,n):
        space = space + "  "
    star = ""
    for k in range(1,i+1):
        star = star + "* "
    print(space+star)        
'''
'''
n = 5
for i in range(1,n+1):
    space = ""
    for j in range(1,i):
        space = space +"  "
    star = ""
    for k in range(i,n+1):
        star = star + "* "
    print(space + star)
'''
'''
n = 4
for i in range(1,n+1):
    space = ""
    for j in range(i,n):
        space = space + "  "
    star = ""
    for k in range(1,i+1):
        star = star + "* "    
    for l in range(1,i):
        star = star + "* "
    print(space + star) 
'''
'''
n = 4
for i in range(n,0,-1):
    space = ""
    for j in range(i,n):
        space = space + "  "
    star = ""
    for k in range(1,i+1):
        star = star + "* "    
    for l in range(1,i):
        star = star + "* "
    print(space + star)
'''
'''
n = 4
for i in range(1,n+1):
    space = ""
    for j in range(i,n):
        space = space + "  "
    star = ""
    for k in range(1,i+1):
        star = star + "* "    
    for l in range(1,i):
        star = star + "* "
    print(space + star)    
for i in range(n-1,0,-1):
    space = ""
    for j in range(i,n):
        space = space + "  "
    star = ""
    for k in range(1,i+1):
        star = star + "* "    
    for l in range(1,i):
        star = star + "* "
    print(space + star)
'''
'''
n = 3

for i in range(1, n + 1):
    star1 = ""
    for j in range(1, i + 1):
        star1 += "* "

    space = ""
    for k in range(1, 2 * (n - i) + 1):
        space += "  "

    star2 = ""
    for j in range(1, i + 1):
        star2 += "* "

    print(star1 + space + star2)

for i in range(n - 1, 0, -1):
    star1 = ""
    for j in range(1, i + 1):
        star1 += "* "

    space = ""
    for k in range(1, 2 * (n - i) + 1):
        space += "  "

    star2 = ""
    for j in range(1, i + 1):
        star2 += "* "

    print(star1 + space + star2)
    
'''
'''
n= 4 
for i in range(1,n+1):
    space = ""
    for j in range(i,n):
        space = space + "  "
    star = ""
    for k in range(1,i+1):
        star = star + "* "
    print(space + star)
for i in range(n-1,0,-1):
    space = ""
    for j in range(i,n):
        space = space + "  "
    star = ""
    for k in range(1,i+1):
        star = star + "* "
    print(space + star)
'''
'''
n= 4 
for i in range(1,n+1):
    space = ""
    for j in range(1,i):
        space = space + "  "
    star = ""
    for k in range(i,n+1):
        star = star + "* "
    print(space + star)
for i in range(1,n+1):
    space = ""
    for j in range(i,n):
        space = space + "  "
    star = ""
    for k in range(1,i+1):
        star = star + "* "
    print(space + star)    
'''
'''
n = 4
for i in range(1,n+1):
    star = ""
    for j in range(1,n+1):
        if i == 1 or i==n:
            star = star + "* "
        elif j == 1 or j == n:
            star = star + "* "
        else:    
            star = star+ "  "
    print(star)        
'''
'''
n = 5
for i in range(1,n+1):
    star = ""
    for j in range(1,i+1):
        if i == 1 or i==n:
            star = star + "* "
        elif j == 1 or j == i:
            star = star + "* "
        else:    
            star = star+ "  "
    print(star) 
'''
'''
n = 5 
for i in range(1,n+1):
    star = ""
    for j in range(1,i+1):
        star = star + (str(j) +" ")
    print(star)                    
'''
'''
n = 5 
for i in range(1,n+1):
    star = ""
    for j in range(1,i+1):
        star = star + (str(i) +" ")
    print(star)         
'''
'''
n = 5

num = 1

for i in range(1, n + 1):
    row = ""
    
    for j in range(1, i + 1):
        row = row + str(num) + " "
        num = num + 1
    
    print(row)            
                
n = 5

for i in range(1, n + 1):
    row = ""
    
    for j in range(i, 0, -1):
        row = row + str(j) + " "
    
    print(row)                
'''    

