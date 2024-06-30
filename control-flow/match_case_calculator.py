num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operations = input('Choose the operation (+, -, *, /): ')

match operations:
  case '+':
    print(f'The result is {num1 + num2:.2f}')  # Format addition result to 2 decimals
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
