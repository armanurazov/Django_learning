# basic function syntax

def say_hello(name):
    return f'hello {name}'

str1 = say_hello('Arman')
print(str1)



# exercise 1

def less_or_greater(num1, num2):
    if num1 < num2:
        return f'{num1} is less than {num2}'
    elif num1 > num2:
        return f'{num1} is greater than {num2}'
    else:
        return f'{num1} equals to {num2}'

str2 = less_or_greater(10, 20)
print(str2)

# exercise 2

def check_lenght(list):
    n = 0
    for i in list:
        n += 1
    return n

my_list = [1,3,6,8,5,4,3,5,6]
print(check_lenght(my_list))

# exercise 3

def calculator(a,b,operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    else:
        return 'function is not supported'

print(calculator(1,10,'-'))
