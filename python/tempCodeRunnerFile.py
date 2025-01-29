
# #decorators

def decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper

@decorator
def hello():
    print("hello world")

@decorator
def hello1():
    print("hello1")    

hello()
hello1()
