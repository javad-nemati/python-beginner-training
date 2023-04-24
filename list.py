list = [2, 4, 1, 12, 37, 9]
print(list)
print(list[0])
print("Largest number is:" , max(list))

numbers = [20, 52, 2, 34]
x = numbers[0]
for num in numbers:
    if num > x:
        x = num
print(x)
print ("second list" , max(numbers))

matrix = [
    [1, 2, 3],
    [4, 5 ,6],
    [7, 8, 9]
]
print(matrix)
matrix[1][2] = 69
print(matrix[1][2])

for row in matrix:
    for item in row:
        print(item)