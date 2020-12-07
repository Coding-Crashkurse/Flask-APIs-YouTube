### Closures
def outer(msg):
    def inner():
        print(msg)

    inner()


outer("Hi")


def outer2(msg):
    def inner():
        print(msg)

    return inner


msg = outer2("Hi")
msg()

outer2("Hi")()


def makeMultiplyer(x):
    def multiplyer(y):
        return x * y

    return multiplyer


f1 = makeMultiplyer(2)
f2 = makeMultiplyer(5)

f1(3)
f2(3)

## Decorators
def greet():
    print("Hallo :-)")


def decorate(func):
    def wrapper():
        print("****************")
        func()
        print("****************")

    return wrapper


def greet2():
    print("Hallo :-)")


greet2 = decorate(greet2)
greet2()


@decorate
def greet3():
    print("Hallo :-)")


greet3()


@decorate
def greet4(name):
    print(f"Hello, I am {name}")


greet4("Markus")


def better_decorate(func):
    def wrapper(*args, **kwargs):
        print("****************")
        func(*args, **kwargs)
        print("****************")

    return wrapper


@better_decorate
def greet4(name):
    print(f"Hello, I am {name}")


greet4("Markus")


def performance(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} braucht {(end - start)} Sekunden')
    return wrapper

@performance
def long_list(n):
    return list(range(n))

long_list(100000000)
