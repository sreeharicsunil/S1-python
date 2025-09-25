#4) a list of integer,for values that are over 100 ,replace them with "over"

nums = "10 100 95 800 64 2 945"

num_list = nums.split()

result = []

for i in num_list:
    i = int(i)
    if i > 100 :
        result.append("over")
    else:
        result.append(i)

print("the processed list is :" , result)
