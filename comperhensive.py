some_list = ['a', 'b', 'c', 'b', 'a', 'd', 'b', 'd']


duplicated = list(set([x for x in some_list if some_list.count(x) > 1]))
duplicated.sort()
print(duplicated)