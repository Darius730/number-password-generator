import random

def password():
    for i in range(6):
        yield random.randint(1213231000, 9994345555600)
        yield random.randint (100000, 9000000)

for random_password in password():
    print("The generated password is: %d" % (random_password))
