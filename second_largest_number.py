nums=list(map(int,input("Enter numbers : ").split()))
large=0
slarge=0
for num in nums:
    if num > large:
        slarge = large
        large = num
    elif num > slarge and large != num:
        slarge = num
print (slarge)

