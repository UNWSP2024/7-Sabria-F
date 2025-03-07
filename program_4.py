#By: Sabria Fafach
#Date: March 7, 2025
#Title: program_4.py


# define main function:
def main():

    #Have the user input the coordinates:
    try:
        x1=float(input("Enter the first x-coordinate:"))
        y1=float(input("Enter the first y-coordinate:"))
        z1=float(input("Enter the first z-coordinate:"))

        x2=float(input("Enter the second x-coordinate:"))
        y2=float(input("Enter the second y-coordinate:"))
        z2=float(input("Enter the second z-coordinate:"))
    except:
        print("You must input a number. Try again.")

#Put coordinates into lists and convert to tuples:
    coordinates_list1=[x1,y1,z1]
    coordinates_tuple1=tuple(coordinates_list1)

    coordinates_list2=[x2,y2,z2]
    coordinates_tuple2=tuple(coordinates_list2)

#Calculate and display the distance between the two points:
    distance=calculate_distance(coordinates_tuple1,coordinates_tuple2)
    print(f"The distance between the two points you entered is {distance:0.2f}.")


#Define the calculate_distance function to calculate the distance between the two points:
def calculate_distance(coordinates_tuple1,coordinates_tuple2):
    distance=((coordinates_tuple2[0]-coordinates_tuple1[0])**2 + (coordinates_tuple2[1]-coordinates_tuple1[1])**2 + (coordinates_tuple2[2]-coordinates_tuple1[2])**2)**.5
    return distance

# Call main function:
if __name__ == '__main__':
    main()