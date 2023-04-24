numbers = [2 , 49, 2 , 30, 2, 49]
numbers.sort()
print(numbers)
numbers2 = numbers.copy()
numbers2.append(10)
print(numbers2)
numbers3 = numbers2.copy()
numbers3.insert(3 , 10)
print(numbers3)
print(numbers3.index(30))
print(49 in numbers3)
numbers3.sort()
print(numbers3)
result = []
for i in numbers3:
    if i not in result:
        result.append(i)
print("the result after remove duplicated item is " + str(result))
tuple