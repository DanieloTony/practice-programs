# here we write a program for sum the given numbers


# Get the count of numbers from user
n = int(input("Enter how many numbers you want to add: "))

# Create empty list to store numbers
numbers = []

# Get each number from user
for i in range(n):
    num = int(input(f"Enter number {i+1}:"))
    numbers.append(num)

print(sum(numbers))
