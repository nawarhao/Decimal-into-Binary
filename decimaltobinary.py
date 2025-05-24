# Decimal to Binary without using bin()

# Get input from user
decimal_number = float(input("Enter a decimal number: "))

binary_number = ""

# Loop to divide the number by 2 and store the remainder
while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number
    decimal_number = decimal_number // 2

# Handle case for 0
if binary_number == "":
    binary_number = "0"

print("Binary number is:", binary_number)
