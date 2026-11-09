nums=list(map(int,input("Enter data : ").split()))
large=0
for num in nums:
    if num > large:
        large=num
print(f"{large} is the largest number in you list")