def test(*args, **kwargs):
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


test(5, 'Вася', True, cat='мяу')


def factorial(n):
    if n == 1:
        return 1
    a = factorial(n=n - 1)
    return n * a


print(factorial(10))


