import calculatemonthoryear

choose_the_M_or_Y = input("Do you want Month or Year both (y/n)? ")
try:
    if choose_the_M_or_Y == "y":
        obj_Calculate = calculatemonthoryear.CalculateMonthOrYear()
        obj_Calculate.month_year_function()

    elif choose_the_M_or_Y == "n":
        months = input("Want the data according to months or year (year/month)? ")

        if months == "month":
            obj_Calculate = calculatemonthoryear.CalculateMonthOrYear()
            print(obj_Calculate.month_func())

        elif months == "year":
            obj_Calculate = calculatemonthoryear.CalculateMonthOrYear()
            print(obj_Calculate.year_func())
    else:
        print("You have entered wrong input")

except Exception as ex:
    print(f"Wrong input: {ex}")
