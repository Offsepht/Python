def double(arg):
    print('Before: ', arg)
    arg *= 2
    print('After: ', arg)


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)

print(double(10))
print(double('Hello '))
numbers = [42,256,16]
print(double(numbers))

