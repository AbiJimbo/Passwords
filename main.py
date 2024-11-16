import random
a ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
b=int(input("Cual es la longitud la contraseña:"))
password=""
for i in range(b):
    password += random.choice(a)
print("La contraseña es:", password)
