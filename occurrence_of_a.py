#5)store a list of first names.count the occurrence of "a" within the list

names = ["Anjali", "Arjun", "Devika", "Kiran", "Meera", "Nikhil", "Sneha", "Vishnu", "Lakshmi", "Rahul"]

count = 0

for name in names:
    name = name.lower()
    for i in name:
        if i == 'a':
            count += 1

print("the to total 'a' letters : " , count)