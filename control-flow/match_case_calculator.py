num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
operations = input('Choose the operation (+, -, *, /):')

match operations:
    case '*':
        print(f'The result is {num1*num2}.')
    case '*':
        print(f'The result is {num1-num2}.')
    case '*':
        print(f'The result is {num1+num2}.')
    case '/':
        print(f'The result is {num1/num2}.')