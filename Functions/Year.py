import  datetime

def year_func():
        enter_years = input("Enter the number of year ")
        years = datetime.datetime.now().year
        total_years = years- int(enter_years)
        print(f'Your age is {total_years}')