# # Brute
# nums = list(map(int,input("Enter numbers into array : ").split()))
# k = int(input("Enter your target : "))
# maxlen=0
# s=0
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         s += nums[j]
#         if s <= k:
#             maxlen = max(maxlen,j-i+1)
#         else:
#             break
# print(maxlen)


# # Better
nums = list(map(int,input("Enter numbers into array : ").split()))
k = int(input("Enter your target : "))
maxlen=0
l=0
r=0
s=0
while(r < len(nums)):
    s +=nums[r]
    while(s > k):
        s -= nums[l]
        l +=1
    if s <= k:
        maxlen=max(maxlen,r-l+1)
        r +=1
print(maxlen)

