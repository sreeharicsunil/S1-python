#13)collect a list of colours separated by commas from the user and print the first and last colours.

colo = str(input("Enter colours separated by commas: "))

list_col = colo.split(",")

print("The first and last colours are : " , list_col[0] + " , " + list_col[-1] )