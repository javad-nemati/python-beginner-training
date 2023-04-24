gusee_limit = 1
while gusee_limit <= 5:
    print("*" * gusee_limit)
    gusee_limit = gusee_limit + 1

secret_number = 9
gusee_limit = 3
gusee_count = 0
while gusee_count < gusee_limit:
    gusee = int(input("Gusss a number: "))
    gusee_count += 1
    if gusee == secret_number:
        print("You Won!")
        break
else:
    print("You Faild")


