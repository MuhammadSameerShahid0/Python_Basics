import  datetime
import MonthsDic

def month_func():
        asking_month_remember = input("Do you want to enter the month in number ? (y/n) ")

        try:
            if asking_month_remember == "y":
                enter_month = input("Enter the month in number ")

                today_month = datetime.date.today().month
                total_months = abs(today_month - int(enter_month))
                month_number_return = f'The remaining months in your birth is {total_months}'
                return  month_number_return

            elif asking_month_remember == "n":
                enter_months = input("Enter the month ")

                month = datetime.datetime.now().month
                enter_months = MonthsDic.MonthDicClass.months_dict(enter_months)

                total_month = month - int(enter_months)

                if total_month < 0:
                    total_month = abs(total_month)
                    month_return = f'The remaining months in your birth is {total_month}'
                    return month_return
                elif enter_months < month:
                    total_month = (12 - month) + enter_months
                    month_return = f'The remaining months in your birth is {total_month}'
                    return month_return
                else:
                    month_return = f'The remaining months in your birth is {total_month}'
                    return month_return
            else:
                return f'Your entered value is invalid'

        except Exception as ex:
            print(f'An error has occurred: {ex}')

