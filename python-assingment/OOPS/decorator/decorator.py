
#simple function
def i(x):
    return x+1

def opearate(fun,x):
    a=fun(x)
    return a
y=int(input("Ente valu of a:"))
c=opearate(i,y)
print(c)


def printer():
    print("hello")

def display(fun):

    def inner():
        print("Executing")
        fun()
        print("Finished executing")
        pass
    return inner

a=display(printer)
a()


# uisng the @method function


def display(fun):

    def inner():
        print("Executing")
        fun()
        print("Finished executing")

    return inner
@display
def printer():
    print("hello")

printer()
# use of iter function

tuple=("hello","mohan")
myit=iter(tuple)
print(next(myit))


def decor(num):
    print("i am decor")

    def inner():
        a=num()
        add= a+10
        return add
    return inner

@decor
def num():
    return 10

b=num()
print(b)