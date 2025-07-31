import datetime
import MonthsDic

def month_year_func():
    try:
        enter_month = input("Enter the month ")
        enter_year = input("Enter the year ")

        month = datetime.datetime.now().month
        year = datetime.datetime.now().year

        month_dic = MonthsDic.MonthDicClass.months_dict(enter_month)

        total_year = year - int(enter_year)
        total_month = month - int(month_dic)

        if total_month < 0:
            total_year = total_year - 1
            total_month = abs(total_month)
            print(f'Your age is {total_year} and birth month is near to {total_month} months')
        elif month_dic < month:
            total_month = (12 - month) + month_dic
            print(f'Your age is {total_year} and birth month is near to {total_month} months')
        else:
            print(f'Your age is {total_year} and birth month is near to {total_month} months')

    except Exception as ex:
        print(f"Wrong input : {ex}")
