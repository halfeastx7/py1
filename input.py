# # a = input ("What is your name: ")
# # print("My name is", a)

# # x= input("Enter a number: ")
# # y= input("Enter another number: ") 
# # # print (x+y)
# # print (int(x) + int(y))

# # name = input ("Enter your name: ")
# # age = input ("Enter your age: ")

# # age = int(age)

# # print("Hello " +name+ ", is " +str(age)+ ", years old")

# # # Single-line strings
# # single_line = "Hello, world!"
# # another_single_line = 'Python is fun!'

# # # Multi-line strings
# # multi_line = """This is a
# # multi-line string
# # spanning several lines."""

# # greeting = "Hello, "
# # name = "Alice"
# # message = greeting + name
# # print(message)  # Output: Hello, Alice

# # laugh = "ha"
# # print(laugh * 3)  # Output: hahaha


# # text = "Python"
# # print(text[0])  # Output: P
# # print(text[1])  # Output: y

# #slicing string
# # a = "python"
# # print(a[1:4:0])

# # Define a string
# fruit = "Mango"

# # Get the length of the string
# mangoLen = len(fruit)
# print("Length of the fruit string:", mangoLen)  # Output: 5

# # Print substrings with explanations

# # Print characters from index 0 to 3 (inclusive)
# print(fruit[0:4])  # Output: Mang

# # Print characters from index 1 to 3 (inclusive)
# print(fruit[1:4])  # Output: ang

# # Print characters from the beginning to index 4 (exclusive)
# print(fruit[:5])  # Output: Mango

# #A Print characters from index 0 to 2 (inclusive)
# print(fruit[0:-3])  # Output: Man

# # Print characters from the beginning to index 2 (exclusive)
# print(fruit[:len(fruit) - 3])  # Output: Man

# # Print characters from index -1 (last character) to index -3 (exclusive)
# print(fruit[-3:len(fruit) - 1])  # Output: g

# # Print characters from index -3 to -2 (exclusive of -1)
# print(fruit[-3:-1])  # Output: ng

 # Example string
# a = "!!!Harry!! !!!!!!!!! Harry"
    
#     # Length of the string
# print("Length of a:", len(a))  # Output: Length of a: 29
    
#     # Original string
# print("Original string:", a)  # Output: !!!Harry!! !!!!!!!!! Harry
    
#     # Convert to uppercase
# print("Uppercase:", a.upper())  # Output: !!!HARRY!! !!!!!!!!! HARRY
    
#     # Convert to lowercase
# print("Lowercase:", a.lower())  # Output: !!!harry!! !!!!!!!!! harry
    
#     # Remove trailing '!'
# print("Right stripped of '!':", a.rstrip("!"))  # Output: !!!Harry!! !!!!!!!!! Harry

# # Replace 'Harry' with 'John'
# print("Replace 'Harry' with 'John':", a.replace("Harry", "John"))  # Output: !!!John!! !!!!!!!!! John
    
#     # Split the string by spaces
# print("Split by space:", a.split(" "))  # Output: ['!!!Harry!!', '!!!!!!!!!!!', 'Harry']
    
    # Capitalize the first letter of each word
# blogHeading = "introduction tO jS"
# print("Capitalized:", blogHeading.capitalize())  # Output: Introduction to js
    
    # String methods with different strings
str1 = "Welcome to the Console!!!"
print("\nString:", str1)
    
    # Length of the string
print("Length of str1:", len(str1))  # Output: Length of str1: 21
    
    # Center align with padding
print("Centered string:", str1.center(50))  # Output: '               Welcome to the Console!!!               '
    
    # Count occurrences of 'Harry'
# print("Count of 'Harry':", a.count("Harry"))  # Output: 2
    
    # Check if the string ends with '!!!'
str1 = "Welcome to the Console !!!"
print("Ends with '!!!':", str1.endswith("!!!"))  # Output: True

str2 = "  "  # using tab
print("Is space (with tab):", str2.isspace())  # Output: True
    
    # Check if the string is in title case
str1 = "World Health Organization"
print("Is title case:", str1.istitle())  # Output: True
    
str2 = "To kill a Mocking bird"
print("Is title case (example 2):", str2.istitle())  # Output: False
    
    # Check if the string starts with 'Python'
str1 = "Python is an Interpreted Language"
print("Starts with 'Python':", str1.startswith("Python"))  # Output: True
    
    # Swap case of all characters
str1 = "Python is an Interpreted Language"
print("Swapped case:", str1.swapcase())  # Output: pYTHON IS AN iNTERPRETED lANGUAGE
    
    # Convert to title case
str1 = "His name is Dan. Dan is an honest man."
print("Title case:", str1.title())  # Output: His Name Is Dan. Dan Is An Honest Man.

# Check if the string ends with 'to' between indices 4 and 10
print("Ends with 'to' between indices 4 and 10:", str1.endswith("to", 4, 10))  # Output: True
    
    # Find the position of a substring (returns -1 if not found)
str1 = "He's name is Dan. He is an honest man."
print("Find 'ishh':", str1.find("ishh"))  # Output: -1
    
    # Check if the string consists of alphanumeric characters
str1 = "WelcomeToTheConsole"
print("Is alphanumeric:", str1.isalnum())  # Output: True
    
    # Check if the string consists of only alphabetic characters
str1 = "Welcome"
print("Is alphabetic:", str1.isalpha())  # Output: True
    
    # Check if the string is in lowercase
str1 = "hello world"
print("Is lowercase:", str1.islower())  # Output: True
    
    # Check if the string is printable
str1 = "We wish you a Merry Christmas\n"
print("Is printable:", str1.isprintable())  # Output: False
    
    # Check if the string contains only whitespace
str1 = "         "  # using spacebar
print("Is space:", str1.isspace())  # Output: True

str2 = "  "  # using tab
print("Is space (with tab):", str2.isspace())  # Output: True
    
    # Check if the string is in title case
str1 = "World Health Organization"
print("Is title case:", str1.istitle())  # Output: True
    
str2 = "To kill a Mocking bird"
print("Is title case (example 2):", str2.istitle())  # Output: False
    
    # Check if the string starts with 'Python'
str1 = "Python is an Interpreted Language"
print("Starts with 'Python':", str1.startswith("Python"))  # Output: True
    
    # Swap case of all characters
str1 = "Python is an Interpreted Language"
print("Swapped case:", str1.swapcase())  # Output: pYTHON IS AN iNTERPRETED lANGUAGE
    
    # Convert to title case
str1 = "His name is Dan. Dan is an honest man."
print("Title case:", str1.title())  # Output: His Name Is Dan. Dan Is An Honest Man.
