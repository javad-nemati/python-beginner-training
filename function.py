

def say_hello(name = 'default' ,emoji = '):'):
    print(f'hellooooo {name} {emoji}')




def super_func(name, *args, i='hi' ,**kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return print(name,sum(args) + total)


print(super_func('javad', 1,2,3,4,5, num1=5, num2=10))

