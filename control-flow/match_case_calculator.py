num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
operations = input('Choose the operation (+, -, *, /):')

match operations:
    case '*':
        print(f'The result is {num1*num2:d}.')
    case '-':
        print(f'The result is {num1-num2:d}.')
    case '+':
        print(f'The result is {num1+num2:d}.')
    case '/':
    if num2 == 0 or num1 == 0 :
      print("Cannot divide by zero.")
    else:
      print(f'The result is {num1 / num2:.2f}')
  case _:
    print("Invalid operation")
