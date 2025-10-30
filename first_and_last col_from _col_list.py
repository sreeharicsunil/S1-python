#15)from a coma separated set of colours got from the user print the first and last colour from the list

col_list = str(input("Enter a set of colours coma separated : "))
list = col_list.split(",")
print(f"The first and last colours are {list[0]} and {list[-1]} ")