#6)Enter 2 lists of integers . a. whether the lists are of the same length . b. whether list sums to same value . c. whether any value occur in both.
list_one = "10 20 30 80 40 50"
list_two = "15 25 35 45"

list_one = list(map(int , list_one.split()))
list_two = list(map(int , list_two.split()))

#a.

if len(list_one) == len(list_two):
    print("Lists are of the same length")
else:
    print("Lists are not of the same length")

#b.
sum_1 = 0
sum_2 = 0

for i in list_one:
    sum_1 = sum_1+i
for i in list_two:
    sum_2 = sum_2 + i

if sum_1 == sum_2:
    print("Both lists have the same sum")
else:
    print("Lists have different sum")

#3.

element = []

for i in list_one:
    for j in list_two:
        if i == j:
            element.append(i)

if len(element) == 0:
    print ("there are no same elements")
else:
    print("the commen elements are :" , element)