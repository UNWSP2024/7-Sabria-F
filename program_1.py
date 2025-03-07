#By: Sabria Fafach
#Date: March 3, 2025
#Title: program_1.py

MONTH_NAMES=["1, January", "2, February", "3, March", "4, April", "5, May", "6, June", "7, July", "8, August", "9, September",
             "10, October", "11, November", "12, December"]

#This function gets the amount of rain per month from the user and appends the values into a list:
def get_monthly_rainfall():
    monthly_rainfall=[]
    for month in MONTH_NAMES:
        rainfall=float(input(f"Enter the rainfall for month {month} in inches:"))
        monthly_rainfall.append(rainfall)
    return monthly_rainfall

#This function calculates the sum of all the values in the list:
def Calculate_total_rainfall(monthly_rainfall):
    total_rainfall=0
    for number in monthly_rainfall:
        total_rainfall+=number
    return total_rainfall

#This function finds the name of the month with the most rain:
def find_wetest_month(monthly_rainfall):
    most_rain=max(monthly_rainfall)
    wetest_month=monthly_rainfall.index(most_rain)
    return wetest_month

#This function finds the name of the month with the least rain:
def find_driest_month(monthly_rainfall):
    least_rain=min(monthly_rainfall)
    driest_month=monthly_rainfall.index(least_rain)
    return driest_month



def main():

#Call the get_monthly_rainfall function:
    monthly_rainfall=get_monthly_rainfall()

#Call the Calculate_total_rainfall function and display total rainfall:
    total_rainfall=Calculate_total_rainfall(monthly_rainfall)
    print(f"The total rainfall is {total_rainfall:.1f}in.")

#Calculate and display the total monthly rainfall:
    average_rainfall=total_rainfall/len(monthly_rainfall)
    print(f"The average rainfall is {average_rainfall:.1f}in/mo.")

#Call the find_wetest_month function and display the wetest month:
    wetest_month=find_wetest_month(monthly_rainfall)
    print(f"The wettest month of the year was {MONTH_NAMES[wetest_month]}.")

#Call the find_driest_month function and display the driest month:
    driest_month = find_driest_month(monthly_rainfall)
    print(f"The driest month of the year was {MONTH_NAMES[driest_month]}.")

if  __name__ == '__main__':
    main()




