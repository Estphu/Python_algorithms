################### QUESTIN 1 ######################

# Implement a python decorator that logs the invocation of the decorated function
# to the provided file descriptor. You can assume that it will only take in positional arguments.
# The log line should follow this format: LOG: <function_name> (<comma_separated_call_parameters>).
# The last character should be a newline.

################### ANSWER 1 ########################

import functools

def log_invocation(file_descriptor):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            params = ','.join(map(repr, args))
            log_line = f'LOG: {func.__name__}({params})\n'
            file_descriptor.write(log_line)
            file_descriptor.flush()
            return func(*args, **kwargs)
        return wrapper
    return decorator


with open('log.txt', 'a') as log_file:

    @log_invocation(log_file)
    def add(a, b):
        return a+b

    result1= add(1,2)
    result2= add(4,8)
    result3 = add(16,32)

################### QUESTIN 2 ######################

# Given an arbitrary function, return a new function, which, when called, returns
# the result of the original function called with the arguments in reversed order.
# For example, if the original function, f, is a pow function, f(2,3) =  8, 2^3 = 8, then the correct 
# result is a function g, with g(3,2) = 9, because 3^2 = 9. Complete the function in python

################### ANSWER 2 ########################

def reverse_args(func):
    def new_func(*args):
        reversed_args = args[::-1]
        return func(*reversed_args)
    return new_func

def power(base, exponent):
    return base**exponent

result = reverse_args(power)(3,2)


print(result)

################### QUESTIN 3 ######################

# You can use a lambda function with the map function to achieve this.
# Here's a lambda function that squares integers greater than 0 and applies it to an array of arrays 
# with varying numbers of elements:

################### ANSWER 3 ########################

input_data = [[1, 2, -3], [4, -5], [6, 7, 8, 9]]

result = map(lambda row: [x**2 for x in row if x>0],input_data)
output = [list(row) for row in result]

print(result)
print(output)