
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
'''
'''
def maxprice(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        if price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit
prices = [5,1,3,7,4]
print(maxprice(prices))        
'''
'''
#leetcode 88
#n = 3
#m = 3

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

m = 3
n = 3

i = 0
j = 0

res = []

while i < m and j < n:
    if nums1[i] < nums2[j]:
        res.append(nums1[i])
        i += 1
    else:
        res.append(nums2[j])
        j += 1

while i < m:
    res.append(nums1[i])
    i += 1

while j < n:
    res.append(nums2[j])
    j += 1

for k in range(m + n):
    nums1[k] = res[k]

print(nums1)
'''            
'''
#leetcode 53


#Check if an Array is Sorted

def is_sorted(arr):
    for i in range(1,len(arr)):
        if(arr[i-1] > arr[i]):
            return False
    return True 
   
arr = [1,2,8,4,5]
print(is_sorted(arr))


#Left Rotate an Array by One Position
def rotate(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr
arr = [1,2,8,4,5]
print(rotate(arr))
'''
'''
class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(0,len(nums)):
            x = target-nums[i]
            if x in map:
                return i,map[x]
            else:
                map[nums[i]] = i 
nums = [3,4,6,2,7,1]
target = 8               
obj = Solution()
print(obj.twoSum(nums,target))        
    
d = {"a":1,"b":2,"c":3}
print(d["b"])

class Solution(object):
    def merge(self, nums1, m, nums2, n): #num1 = [1,2,3,0,0,0] n = 3 num2 = [2,5,6] m = 3 n = 3

        i = 0#3
        j = 0#2

        res = []#[1,2,2,3,5,6]

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < m:
            res.append(nums1[i])
            i += 1

        while j < n:
            res.append(nums2[j])
            j += 1

        for k in range(m + n):
            nums1[k] = res[k]
'''
'''
def rotate(num,t):
    low = 0
    high = len(num)-1
    while(low <= high):
        mid = (low + high)//2
        if(num[mid] == t):
            return num[mid]
        if (num[low] <= num[mid]):
            if(t>=num[low] and t<num[high]):
                high = mid - 1
            else:
                low = mid + 1
        else:
            if (t > num[mid] and t <= num[high]):
                low = mid + 1
            else:
                high = mid-1
num = [4,5,6,7,0,1,2]
t = 0
print(rotate(num,t))

class Solution(object):
    def findMissingAndRepeatedValues(self, a):
        d = {}
        n = len(a)
        for i in a:
            for j in i:
                d[j] = d.get(j,0)+1
        missing = 0
        repating = 0
        for k in range(1,n*n+1):
            if k not in d:
                missing = k
            elif d[k] == 2:
                repating = k
        return [repating,missing,]    
'''
'''
def selection(num):
    n = len(num)
    for i in range(0,n):
        min_value = i
        for j in range(i+1,n):
            if num[j] < num[min_value]:
                min_value = j
        temp = num[i]
        num[i] = num[min_value]
        num[min_value] = temp
num = [1,3,2,4,6,5]
selection(num)
print(num)


def bubble(num):
    n = len(num)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if num[j] > num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
    print(num)
bubble([1,3,2,4,6,5])                
'''
'''
def insertion(num):
    n = len(num)
    for i in range(1,n-1):
        j = i
        while(j > 0 and num[j-1] < num[j]):
            num[j] = num[j-1]
    print(num)
insertion([1,3,2,4,6,5])
'''
#move all zeros to the end using two pointers
a = [0,1,0,3,12]
n = len(a)
j = 0
for i in range(n):
    if a[i] != 0:
        a[j],a[i] = a[i],a[j]
        j = j + 1
print(a)

#remove duplicates from sorted array using two pointers
a = [1,1,2,2,3,3,4,5,5,6,7,7]
n = len(a)
j = 0
for i in range(1,n):
    if a[i] != a[j]:
        j = j + 1
        a[j] = a[i]
print(a[:j+1])   

# reverse an array using two pointers
a = [1,2,3,4,5]
i = 0
j = len(a)-1
while i < j:
    a[i],a[j] = a[j],a[i]
    i = i+1
    j = j-1
print(a)
# check if an array is palindrome using two pointers
a = [1,2,3,3,1]
i = 0
j = len(a)-1
is_palidrome = True
while i < j:
    if a[i]!= a[j]:
        is_palidrome = False
        break
    i = i+1
    j = j-1
print(is_palidrome)
# find intersection of two arrays using two pointers
a = [1,2,3,4]
b = [2,2,3,5]
c = []
i = 0
while i<len(b):
    j = 0
    while j < len(a):
        if b[i] == a[j]:
            if b[i] not in c:
                c.append(b[i])
                break
        j = j+1
    i = i +1
print(c)
# find two sum using two pointers   
n = [2,11,15]
t = 9
i = 0
j = len(n)-1
is_found = False
while i < j:
    total = n[i] + n[j]
    if t == total: 
        print(i,j)
        is_found = True
        break
    elif total > t:
        j = j-1
    else:
        i = i + 1
if not is_found:
    print(None)
    
#majority element using two pointers    
a =[1,2,2,1,1,1,1,1,3,4,10,1,5,6,7,8,2,2,2,1,2,2,1,2]
d = {}
for i in a:
    d[i] = d.get(i,0)+1
max_count = 0
found = None    
for j in d:
    if d[j] > max_count:
        max_count = d[j]
        found = j
print(found)                   
  
