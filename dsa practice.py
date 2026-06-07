
'''
arr = [1,2,0,3,4,0,0,0]
zero = []
non_zero = []
for i in range(0,len(arr)-1):
    if arr[i] == 0:
        zero.append(arr[i])
    else:
        non_zero.append(arr[i])                    
non_zero.extend(zero)
print(non_zero)  
'''
'''
def arr(num):
    i = 0#4
    j = 0#6
    while(j <= len(num)-1):
        if(num[j]!= 0):#3
            temp = num[i]#0
            num[i] = num[j]#3
            num[j] = temp #0  
            i = i+1
        j = j+1
    return num
num = [1,3,0,3,0,2,6,0,8,0] 
print(arr(num)) 

'''
'''
arr = [1,1,2,2,3,3,4]
res = []
for i in range(0,len(arr)-1):
    if arr[i] not in res:
        res.append(arr[i])
print(res)
'''

def unique(arr):
    i = 0 
    j = 1
    while(j <= len(arr)-1):
        if (arr[i] != arr[j]):
            arr[i+1] = arr[j]
            i = i + 1
        j = j+1
    return arr
arr = [1,1,2,2,3,4,4,5]
print(unique(arr))        



        