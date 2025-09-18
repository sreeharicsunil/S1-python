#sreehari c
#display future leap year from current year to a final year entered by user

current_year = int(input("Enter the current year : "))
final_year = int(input("Enter the final year : "))

for year in range (current_year ,final_year + 1):
    if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0 ):
        print(year)
