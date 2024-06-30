num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
Type_of_operation = input('Choose the operation (+, -, *, /):')

match Type_of_operation:
    case '*':
        print(f'The result is {num1*num2}.')
    case '-':
        print(f'The result is {num1-num2}.')
    case '+':
        print(f'The result is {num1+num2}.')
    case '/':
        print(f'The result is {num1/num2}.')