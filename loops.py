# # List of fruits
# fruits = ["apple", "banana", "cherry", "date"]

# # Iterate over the list and print each fruit
# for x in fruits:
#     print(x)

# # Iterate over a range of numbers from 0 to 4
# for i in range(1000):
#     print(i)
# print("Done!!!")

# Example 1: Iterating over each character in a string
# name = 'samraiz'
# for i in name:
#     print(i)
#     if i == 'm':
#         print("This is something special!")

# print()  # Add a blank line for separation

# Example 2: Iterating over a list of colors and printing each character in each color
# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#     print(color)
#     for char in color:
#         print(char)
# print()  # Add a blank line for separation


# # Example 3: Iterating over a range of numbers and printing each number incremented by 1
# for k in range(5):
#     print(k + 1)

# print()  # Add a blank line for separation

# # Example 4: Iterating over a large range of numbers and printing each number
# for k in range(1, 20001):
#     print(k)

# # Prompt user for input and print it
# i = int(input("Enter the number: "))
# print(i)

# # Continue prompting for input while the number is less than or equal to 38
# while i <= 38:
#     i = int(input("Enter the number: "))
#     print(i)

# # Notify user that the loop has ended
# print("Done with the loop")

# # Initialize the sum to 0
# total_sum = 0

# print("Enter positive numbers to add to the sum. Enter a negative number to stop.")

# # Loop until the user enters a negative number
# while True:
#     # Get user input
#     number = float(input("Enter a number: "))

#     # Break the loop if the input is a negative number
#     if number < 0:
#         break

#     # Add the positive number to the total sum
#     total_sum += number

# # Print the final sum
# print("The total sum of positive numbers is:", total_sum)

# Loop through numbers from 1 to 10
for i in range(1, 100):
    print(i)
    if i == 50:
        print("Breaking the loop")
        break  # Exit the loop when i equals 5
