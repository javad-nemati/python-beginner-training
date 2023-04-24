my_list = range(1, 11)
counter = 0
for item in range(11):
    counter += item
print(counter)

for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is : {i}')