def main():
    while True:
        try:
            width = float(input("Enter the width of the area to be fenced (in meters): "))
            length = float(input("Enter the length of the area to be fenced (in meters): "))
            cost_per_meter = float(input("Enter the cost of fencing per meter: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        perimeter = 2 * (width + length)
        total_cost = perimeter * cost_per_meter

        print(f"The perimeter of the area is: {perimeter:.2f} meters")
        print(f"The total cost of fencing is: {total_cost:.2f}")

        another = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()

