from functools import reduce
my_list = [1, 2, 3]
def multiple_by2(item):
    return item*2
print(list(map(multiple_by2, my_list)))
print(my_list)


def accumulator(acc, item):
    print(acc, item)
    return acc + item
print(reduce(accumulator, my_list, 5))
#print(my_list)

print(reduce(lambda acc, item: acc+item, my_list))