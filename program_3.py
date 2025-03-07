#By: Sabria Fafach
#Date: March 7, 2025
#Title: program_3.py

def main():

    enter_state_info=input("Do you want to enter information about a state? (y = yes, anthing else = no):")
    all_entered_values = []
    while enter_state_info=="y":
        year=int(input("Enter the year this data was collected:"))

        state=input("Enter the name of the state:")

        population=int(input(f"Enter the population of {state} in {year}:"))
        
        all_entered_values.append([year,state,population])
        enter_state_info=input("Do you want to enter information about another state? (y = yes, anthing else = no):")

    # Now have the user enter a year. 
    year_to_sum=int(input("Enter the year that you want to sum population for:"))

    # Pass the list and year to the sum_population_for_year
    total_pop=sum_population_for_year(all_entered_values,year_to_sum)

    # print the totalled population
    print(f"The total population for {year_to_sum} is {total_pop} people.")

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    total_pop=0
    for row in all_entered_values:
        if year_to_sum==row[0]:
            total_pop+=row[2]
    return total_pop



# Call the main function.
if __name__ == '__main__':
    main()