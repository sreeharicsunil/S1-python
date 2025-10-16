#12) accept a file name from the user and print the file extension name

name = str(input("Enter the file name "))
d = "."
if d in name:
    ext = name.split(".")
    print("Extension is: " , ext[1] )
else:
    print("incorrect file name.")