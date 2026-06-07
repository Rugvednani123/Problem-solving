# Print All Prime Numbers from m to n
'''
m = 10
n = 30
for i in range(m,n+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count = count +1
    if count == 2:
        print(i ,end = " ")
'''
# Print All Prime Numbers from m to n
'''
m = 10
n = 30
count1 = 0
for i in range(m,n+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count = count +1
    if count == 2:
        count1 = count1+1
print(count1)               
'''
#Print All Armstrong Numbers in a Range
'''
m = int(input("enter the number:"))
n = int(input("enter the number:"))
for i in range(m,n+1):
    temp = i
    digits = len(str(i))
    total = 0
    while temp > 0:
        res = temp % 10
        total = total + res **digits
        temp = temp // 10
    if total == i:
        print(i, end = " ")    
'''
#First Prime Number from m to n
'''
n = 12
m = 25
for i in range(n,m+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count = count +1
    if count == 2:
        print(i)               
        break
'''
'''
n = 20
m = 25
start = n
while (start <=m):
    count = 0
    i = 1
    while(i<=start):
        if start % i == 0:
            count = count +1
        i = i+1
    if count == 2:
        print(start)
        break
    start = start + 1
'''
#Last Prime Number from m to n
'''
n = 30
m = 40
last_prime = -1
for i in range(n,m+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count = count+1
    if count == 2:
        last_prime = i
print(last_prime)            
'''
#First Vowel in a Name
'''
vowels = "aeiouAEIOU"
str = "Rugved"
for i in str:
    if i in vowels:
        print(i)
        break
'''
#Last Vowel in a Name
'''
vowels = "aeiouAEIOU"
str = "Rugved Dasari"
last_vowel = None
for i in str:
    if i in vowels:
        last_vowel = i
print(last_vowel)   
'''
#Print All Even Numbers Using Continue
'''
n = 10
for i in range(1,n+1):
    if i % 2 != 0:
        continue
    print(i)   
'''
#Print All Odd Numbers Using Continue
'''
n = 10
for i in range(1,n+1):
    if i % 2 == 0:
        continue
    print(i)
'''
# Count of Prime and Composite Numbers from m to n
'''
m = 10
n = 50
is_prime = 0
is_composite = 0
for i in range(m,n+1):
    count = 0   
    for j in range(1,i+1):
        if i % j == 0:
            count = count +1
    if count == 2:
        is_prime += 1 
    else:
        is_composite += 1
print("prime Numbers count:",is_prime)
print("composite number count:",is_composite)              
'''
