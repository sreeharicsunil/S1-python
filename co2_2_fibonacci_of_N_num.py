num = int(input("Enter a numer : "))
a = 0
b = 1
c = 0 # store the old value of 'a' temporarily
for i in range(num) :
    print(a)
    c = a
    a = b
    b = b + c