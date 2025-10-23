num = int(input("Enter a numer : "))
count = 1
fac =1
if num < 0 :
    print("Enter a valid number :( ")
elif num == 0 :
    print("The factorial is : ",num)
else:
    while(count <= num):
        fac = fac * count
        count +=1
    print("The factorial is : ",fac)