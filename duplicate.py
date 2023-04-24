some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

uniqlist = []
duplicatelist = []

for item in some_list:
    if item not in uniqlist:

        uniqlist.append(item)
    elif item not in duplicatelist:
        duplicatelist.append(item)

print(duplicatelist)
print(uniqlist)
print(some_list)
