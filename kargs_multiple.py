# def function_name(parameter1, parameter2, *args, **kargs):

# def full_name(first, last):
#     name = f'My Full Name is: {first} {last}'
#     return name

# taking parameter in order(serial wise)
# name = full_name('Abu', 'Naim')

# taking parameter not in order
# name = full_name(last = 'Name', first='Abu')
# print(name)

# def famous(kargs) == key arguments
# def famous_name(first, last, **addition):
#     name = f'{first} {last}'
    # print(addition)
    # print(addition['special'], addition['symbol'])
#     for key, value in addition.items():
#         print(key, ': ', value)
#     return name

# name = famous_name('taheri', 'hujur', special='dhele dei', symbol='vondo', title ='boshe jan')

# print(name)

# multiple return from function

# def multiple_jinish(num1, num2):
#     # as tuple
#     return num1 + num2, num1 - num2, num1 * num2 

#     # as list 
#     return [num1 + num2, num1 - num2, num1 * num2]

# result = multiple_jinish(2,4)
# print(result)
