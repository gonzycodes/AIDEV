from functools import reduce

def hej():
    print("Tja")
    
hej()


def even_odd(x: int) -> str:
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_odd(4))
print(even_odd(3))


def default_args(x, y):
    print("x: ", x)
    print("y:", y)
default_args(5, 10)

def student(fname, lname):
    print(fname, lname)
student("John", "John")


def my_fun(*args):
    print(args)

my_fun(1, 2, 3)
my_fun("a", "b")

def print_doc():
    """Yuh
    """
    print(print_doc.__doc__)
print_doc()

def outer_fun():
    s = "Snakes"
    def inner_fun():
        print(s)
    inner_fun()
outer_fun()

def square(x):
    y = x * x
    return y

square_lambda = lambda x: x * x
print(square(5))
print(square_lambda(7))


def ref_fun(x):
    x[0] = 20
li = [10, 20, 30 ,40 ,50]
ref_fun(li)
print(li)


def ref_fun2(x):
    x = [20, 30, 40]
li = [11, 12, 13]
ref_fun2(li)
print(li)

def countdown(n):
    if n == 0:
        print("Done")
    else:
        print(n)
        countdown(n - 1)
countdown(10)

def multiply(a, b):
    return a * b

def rectangle_are(width, height):
    return multiply(width, height)
print(rectangle_are(5, 3))


numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x + 10, numbers))
print(result)

result = list(filter(lambda x: x > 3, numbers))
print(result)

result = reduce(lambda a,b: a + b, numbers)
print(result)