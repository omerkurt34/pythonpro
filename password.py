import random
semboller = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
 
password_uzunluk = int(input("lütfen parola uzunluğu giriniz ? : "))
password_parola = ""
for i in range(password_uzunluk):
    password_parola += random.choice(semboller)

print(password_parola)    
