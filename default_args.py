# tuple

def all_nums(num1, num2, *args):
    sum = 0
    print(num1, num2, args)
    for num in args:
        print(num)
        sum = sum+num
    print(sum)

all_nums(10,20,30,40, 50)