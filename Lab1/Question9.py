def fib(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)

i = 1
while fib(i) <= 50:
    print(fib(i), end=" ")
    i += 1