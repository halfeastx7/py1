# Loop through numbers from 1 to 10
for i in range(1, 11):
    print(i)
    if i == 5:
        print("Breaking the loop")
        break  # Exit the loop when i equals 5

# Initialize counter
count = 0

# Infinite while loop
while True:
    count += 1
    print("Current count:", count)
    
    # Break the loop when count reaches 7
    if count == 7:
        print("Breaking the loop at count 7")
        break

# Loop through numbers from 1 to 5
for i in range(1, 6):
    if i == 3:
        continue  # Skip the rest of the loop when i is 3
    print("Current number is:", i)

# String to iterate over
word = "Python"

# Loop through each letter in the string
for letter in word:
    if letter == "h":
        continue  # Skip the rest of the loop when the letter is 'h'
    print("Current letter is:", letter)

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through each number in the list
for num in numbers:
    # If the number is even, skip the rest of the loop and continue with the next iteration
    if num % 2 == 1:
        # print(f"Skipping the odd number: {num}")
        continue
    
    # This will only print if the number is 
    print(f"Processing the even number: {num}")
