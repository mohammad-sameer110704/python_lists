# # Brute code O(n*n)
nums=list(map(int,input("Enter numbers : ").split()))
k=int(input("Enter a number"))
summ=[]
l=0
r=k
s=0
while(r <= len(nums)):
    for i in range(l,r):
        s += nums[i]
    summ.append(s)
    r += 1
    l += 1
    s = 0
print(summ)

# # Optimized code O(n)
# nums = list(map(int, input("Enter numbers: ").split()))
# k = int(input("Enter a number: "))

# summ = []
# s = sum(nums[:k])

# summ.append(s)

# for i in range(k, len(nums)):
#     s = s - nums[i-k]
#     s = s + nums[i]

#     summ.append(s)

# print(summ)




