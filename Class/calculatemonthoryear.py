import datetime
from Functions.MonthsDic import MonthDicClass

class CalculateMonthOrYear:
    def __init__(self):  # ctor
        self.current_month = datetime.datetime.today().month
        self.current_year = datetime.datetime.today().year

    def month_year_function(self):
        try:
            enter_month = input("Enter the month ")
            enter_year = input("Enter the year ")

            month_dic = MonthDicClass.months_dict(enter_month)

            total_year = self.current_year - int(enter_year)
            total_month = self.current_month - int(month_dic)

            if total_month < 0:
                total_year = total_year - 1
                total_month = abs(total_month)
                print(f'Your age is {total_year} and birth month is near to {total_month} months')
            elif month_dic < self.current_month:
                total_month = (12 - self.current_month) + month_dic
                print(f'Your age is {total_year} and birth month is near to {total_month} months')
            else:
                print(f'Your age is {total_year} and birth month is near to {total_month} months')

        except Exception as ex:
            print(f"Wrong input: {ex}")

    def month_func(self):
        try:
            asking_month_remember = input("Do you want to enter the month in number ? (y/n) ")

            if asking_month_remember == "y":
                enter_month = input("Enter the month in number ")

                total_months = abs(self.current_month - int(enter_month))
                month_number_return = f'The remaining months in your birth is {total_months}'
                return month_number_return

            elif asking_month_remember == "n":
                enter_months = input("Enter the month ")

                enter_months = MonthDicClass.months_dict(enter_months)
                total_month = self.current_month - int(enter_months)
                if total_month < 0:
                    total_month = abs(total_month)
                    month_return = f'The remaining months in your birth is {total_month}'
                    return month_return
                elif enter_months < self.current_month:
                    total_month = (12 - self.current_month) + enter_months
                    month_return = f'The remaining months in your birth is {total_month}'
                    return month_return
                else:
                    month_return = f'The remaining months in your birth is {total_month}'
                    return month_return
            else:
                invalid = 'Your entered value is invalid'
                return invalid

        except Exception as ex:
            return f"Wrong input: {ex}"

    def year_func(self):
        try:
            enter_year = input("Enter the year: ")
            total_years = self.current_year - int(enter_year)
            result = f'Your age is {total_years}'
            return result
        except Exception as ex:
            print(f"Wrong input: {ex}")
