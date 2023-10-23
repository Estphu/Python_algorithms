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
