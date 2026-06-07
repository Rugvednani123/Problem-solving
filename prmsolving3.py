'''
num = 5
sum = 0
for i in range(1,num+1):
    sum = sum+i
print(sum)
'''
'''
num = 5 
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print(factorial)
'''
'''
num1 = 2
num2 = 10
sum = 0
for i in range(num1,num2+1):
    sum = sum+i
print(sum)
'''
'''
num = 6
count = 0
for i in range(1,num+1):
    if 6 % i == 0:
        count = count+1
        print(i)
print(count)    
 '''
        
'''
num = int(input("enter a number:"))
for i in range(1,num+1):
    count= 0
    for j in range(1,i+1):
        if i % j == 0:
            count = count+1
    if count == 2:
        print(i)
'''
'''
num = 123
sum = 0 
while num > 0:
    sum = sum + num%10
    num = num//10
print(sum)  

num = 153
sum = 0
while num > 0:
    cube = num%10
    sum = sum + cube**3
    num = num // 10
print(sum)
'''
'''
num = 532
reverse = 0
while num > 0:
    reverse = reverse*10 + num%10
    num = num//10
print(reverse)
'''
'''
a = "rugved"
b = []
c = []
for i in a:
    if i not in "aeiou":
        b.append(i)
    else:
        c.append(i)                   
print(len(b))
print(len(c))        
'''