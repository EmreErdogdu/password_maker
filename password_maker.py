import random


karakterler ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sayi = int(input("Kaç karakterden oluşan bir şifreye ihtiyacın var?"))
parola = ""

for i in range(sayi):
    parola += random.choice(karakterler)
    
print("oluşturulan şifre=",parola)
