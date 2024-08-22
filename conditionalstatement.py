# age = int (input("Enter your age: "))
# print ("Your age is: ", age)

# if age >= 18:
#     print ("You are an adult")
# elif age >= 13:
#     print ("You are a teenager")
# else:
#     print ("You are a child")


# # Define the price of apples and the available budget
# applePrice = 10
# budget = 200

# # Check if the remaining budget after buying apples is greater than 50
# if (budget - applePrice > 50):
#     print("Alexa, add 1 kg Apples to the cart.")
# else:
#     print("Alexa, do not add Apples to the cart.")

# Get user input for a number
number = int(input("Enter a number: "))

# # Display the entered number
print("You entered:", number)

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
elif number < 0:
    print("The number is negative.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is zero.")
