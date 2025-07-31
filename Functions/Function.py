import  Month_Year
import  Months
import Year

choose_the_M_or_Y = input("Do you want Month or Year both (y/n)? ")

if choose_the_M_or_Y == "y":
    Month_Year.month_year_func()

elif choose_the_M_or_Y == "n":
    months = input("Want the data according to months or year (year/month)? ")

    if months == "month":
        print(Months.month_func())

    elif months == "year":
        Year.year_func()

else:
    print("You have entered wrong input")