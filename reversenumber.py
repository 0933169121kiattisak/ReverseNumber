number = int(input("Enter a Interger number: "))
operation = input("Enter an operation: ")

if number <= 10:
  print("The number is less than or equal to 10, please enter a number greater than 10")
else:
  reversed_number = int(str(number)[::-1])
  if operation == "+":
    result = reversed_number + number
    print(f"The result of {number} {operation} {reversed_number} is {result}")
  elif operation == "*":
      result = reversed_number * number
      print(f"The result of {number} {operation} {reversed_number} is {result}")
    
    
# --------------------------------------------------------------------------------

def reverse_number(number, operation):
  reversed_number = int(str(number)[::-1])
  if number <= 10:
    print("The number is less than or equal to 10, please enter a number greater than 10")
  else: 
    if operation == "+":
      result = number + reversed_number
      print(f"The result of {number} {operation} {reversed_number} is {result}")
    elif operation == "*":
      result = number * reversed_number
      print(f"The result of {number} {operation} {reversed_number} is {result}")

reverse_number(20,"*")