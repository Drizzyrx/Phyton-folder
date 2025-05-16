# step 3.1: Get the first number from the user
first_number_str = input("Enter the first number: ")
# step 3.2: Get the second number from the user
second_number_str = input("Enter the second number: ")
# step 3.3: Get the operation choice from the user
operation = input("+,-,*,/: ")
# setp 3.4: Convert the number strings to floating-point numbers
try: 
    first_number = float(first_number_str)
    second_number = float(second_number_str)
except ValueError:
    print("Error! Please, enter valid numbers.")
    exit()
# step 3.5: Perform the selected operation 
if operation =='+':
    result = first_number + second_number
elif operation == '-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/':
    if second_number == 0:
        print("Error! Cannot divide by zero.")
        exit()
    else:
        result = first_number / second_number
else:
    print("Invalid operation!")
    exit()

# Step 3.6: Display the result
print("The result is:", result)