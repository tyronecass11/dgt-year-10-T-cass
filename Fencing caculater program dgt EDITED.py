# Assignment 1 Fence Cost Calculator
# Author - Tyrone Cass
# Version 1.0



def main():
    while True:
        try:
            # asking the user to enter the width
            width = float(input("Enter the width of the area to be fenced (in meters): "))
    
            length = float(input("Enter the length of the area to be fenced (in meters): "))# asking the user to enter the length
            cost_per_meter = float(input("Enter the cost of fencing per meter: "))# asking the user to enter the cost of fencing per metre
        except ValueError:
            print("Invalid input. Please enter numeric values.")#If the user types something that's not a number, show an error and ask again
            continue

        perimeter = 2 * (width + length)# Calculating the perimiter
        total_cost = perimeter * cost_per_meter#calculate the total cost

        print(f"The perimeter of the area is: {perimeter:.2f} meters")# print the calculated perimiter
        print(f"The total cost of fencing is: {total_cost:.2f}")# print the calculated cost

        another = input("Do you want to perform another calculation? (yes/no): ").strip().lower() #ask the user if they want to perform another calculation
        if another != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
#run the main function to start the program

