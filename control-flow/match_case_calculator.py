num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operations = input('Choose the operation (+, -, *, /): ')
result = 0
match operations:
  case '+':
    result = num1 + num2:
    print(f'The result is {result}')  # Format addition result to 2 decimals
  case '-':
    print(f'The result is {num1 - num2:.2f}')  # Format subtraction result to 2 decimals
  case '*':
    print(f'The result is {num1 * num2}')
  case '/':
    if num2 == 0:
      print("Cannot divide by zero.")
    else:
      print(f'The result is {num1 / num2:.2f}')  # Format division result to 2 decimals
  case _:
    print("Invalid operation")
