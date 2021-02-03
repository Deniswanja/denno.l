def calculator(first_number, second_number, operation):
    if operation.upper() == 'ADD':
        return(float(first_number) + float(second_number))
    elif operation.upper() =='SUBTRACT':
        return(float(first_number) - float(second_number))
    else:
        return('Invalid operation please specify ADD or SUBTRACT')
# Test your function with the values 6,4, add 
# Should return 10
#
print('Adding 6 + 4 = ' + str(calculator(6,4,'add')))
# Test your function with the values 6,4, subtract 
# Should return 2
print('Subtracting 6 - 4 = ' + str(calculator(6,4,'subtract')))
# Test your function with the values 6,4, divide 
# Should return some sort of error message
print('Dividing 6 / 4 = ' + str(calculator(6,4,'divide')))