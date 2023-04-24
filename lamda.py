my_list = [5, 4, 3]


#for item in my_list:
#   item = item **2
#  print(item)

def square1():

    for item in my_list:
        item = item **2
        print(item)
    return item
    print(item)

def square2(item):
    return item **2

square1(

print(list(map(square2, my_list)))

new_list = list(map(lambda num: num**2, my_list))
print(new_list)

#print(list(map(lambda num, item: num **2, my_list)))
#print(reduce(lambda acc, item: acc+item, my_list))

