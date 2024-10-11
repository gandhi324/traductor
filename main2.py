import random

caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input("introduce la longitud de tu contraseña:"))
resultado=""

for i in range(longitud):
    resultado+=random.choice(caracteres)

print(f"tu contraseña con longitud {longitud} es {resultado}")

