price = 10000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${price}")

name = input("Please Enter a Name: ")
print(name)

if len(name) < 3:
    print("name must be at least 3")
elif len(name) > 10:
    print("name can be maximum 10 character")
else:
    print("name looks good")