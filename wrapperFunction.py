#Decorator

def function(fun):
    def wrapper(*args):
        print("Before calling..")
        fun(*args)
        print("After calling..")
    return wrapper

@function
def test(x, b=4):
    print(x+b)

test(2)