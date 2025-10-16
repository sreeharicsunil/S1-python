# 9) create a string from given string where first and last charactor exchange.

text = input(str("Enter a word : "))

if len(text) > 1:
    new = text[-1] + text[1:-1] + text[0]
else:
    new = text

print("Result is : " , new)