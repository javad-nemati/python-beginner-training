#Error Handling

while True:
    try:
        age = int(input('what is your age: '))
        10/age
    except ValueError:
        print('please Enter an number! ')
    except ZeroDivisionError:
        print('please Enter age higher than Zero!')
    else:
        print('thank you')
        break

