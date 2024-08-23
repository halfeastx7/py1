# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()
# greet()
# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"Isn't the weather nice today {name}?")

# greet_with_name("Rolf")
# greet_with_name("Jen")

# def multiply(x, y):
#     return x * y

# result = multiply(4, 7)
# print(result)

# def check_number(number):
#     if number > 0:
#         return "The number is positive."
#     elif number < 0:
#         return "The number is negative."
#     else:
#         return "The number is zero."

# # Test the function
# print(check_number(10))   # Output: The number is positive.
# print(check_number(-5))   # Output: The number is negative.
# print(check_number(0))    # Output: The number is zero.

# def greet(first_name, last_name):
#     print(f"Hello, {first_name} {last_name}!")

# greet("John", "Doe")

# def greet(first_name, last_name):
#     print(f"Hello, {first_name} {last_name}!")

# greet(last_name="Doe", first_name="John")

# def greet(first_name, last_name="Smith"):
#     print(f"Hello, {first_name} {last_name}!")

# greet("John")         # Uses default last name
# greet("Jane", "Doe")  # Overrides default last name

def greet(*nama):
    for name in nama:
        print(f"Hello, {name}!")

greet("John", "Jane", "Doe")

