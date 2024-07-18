def perform_operation(num1, num2, operation) :
    if operation == 'add' :
         return num1 + num2
    elif operation == 'subtract' :
         return num1 - num2
    elif operation == 'multiply' :
         return num1 * num2
    elif operation == 'divide' and num1 == 0 or num2 == 0:
         return 'Error: Division by zero is not allowed'
    elif operation == 'divide' and num1 != 0 and num2 != 0:
         return num1 / num2

perform_operation(num1, num2, operation)