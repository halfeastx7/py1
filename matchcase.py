# Get user input for the day of the week
day = input("Enter a day of the week: ").strip().lower()

# Match the input day with different cases
match day:
    case "monday":
        print("Start of the work week!")
    case "tuesday":
        print("Second day of the week.")
    case "wednesday":
        print("Midweek day.")
    case "thursday":
        print("Almost there!")
    case "friday":
        print("Last working day of the week!")
    case "saturday":
        print("Weekend starts!")
    case "sunday":
        print("Relax, it’s Sunday.")
    case _:
        print("Invalid day entered.")
