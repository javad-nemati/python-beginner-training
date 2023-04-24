#Decorator
def my_decorator(func):
    def wrap_func():
        print(' O')
        print('-|-')
        print("/ \\")
        func()
        print(' O')
        print('-|-')
        print("/ \\")
    return wrap_func

@my_decorator
def hello():
    print("Hellllloooo")

hello()



def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('#############')
        func(*args, **kwargs)
        print('#############')
    return wrap_func

@my_decorator2
def hello2(greeting, emoji=':('):
    print(greeting, emoji)
hello2('Hiiiiiiii')