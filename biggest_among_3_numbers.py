# 11) find the biggest nuber from the 3 numbers

print ("Enter three valid integer numbers : ")

nums = []
for i in range(3):
    num = int(input(">>>"))
    nums.append(num)

nums.sort()

print("the largest integer is  : " , nums[2])