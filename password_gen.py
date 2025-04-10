from random import choice

def pass_gen(length = 10):
    password_chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(length):
        password += choice(password_chars)
    
    return password
