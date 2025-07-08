""" Butun sonlarga oid masalalar mavusidagi 30 ta masala berilgan """
#integer1
# l = int(input("L uzunlikni kiriting: "))
# num = str(l / 100)
# n,s = num.split('.')
# print(n)

#integer4 
# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))
# soni = A // 
# print(f"B kesma A kesmaga {soni} marta to‘liq joylashadi.")

#integer6
# son = input("Ikki xonali son kiriting: ")
# bir = son[0]
# ikki = son[1]
# print(f"o'nlilar xonasidagi raqam {bir}, birliklar xonasidagi raqam {ikki}")

#integer7
# n = int(input("Ikki xonali son kiriting: "))
# a = n // 10  
# b = n % 10   
# yigindi = a + b
# print(f"Raqamlar yig‘indisi: {yigindi}")

#integer8
# n = int(input("Ikki xonali son kiriting: "))
# a = n // 10  
# b = n % 10   
# teskari = b * 10 +a
# print(f"Raqamlar yig‘indisi: {teskari}")

#integer10
# n = int(input("uch xonali son kiriting: "))
# a = n // 10 
# ikkinchi = a % 10 
# b = n % 10
# print(b) 
# print(ikkinchi)  

#integer16
# n = int(input("uch xonali son kiriting: "))
# a = n // 10 
# onlik = a % 10 
# birlik = n % 10
# yuzlik = n // 100
# teskari_son = yuzlik*100 + birlik*10 + onlik
# print(teskari_son) 

#integer17
# tort_xonali_son = int(input("999 dan katta son = "))
# yuzlik = tort_xonali_son // 100 
# yuzlik_son = str(tort_xonali_son)[-3:]
# print(yuzlik_son)

#integer23
# n = int(input("kun boshidan o'tgan sekundlar: "))
# inhours = n / 3600
# minutes = int((inhours % 1) * 60)
# hours = n // 3600
# qoldiq = n % 3600
# sekunds = qoldiq % 60
# print(f"Kun boshidan boshlab {hours} soat, {minutes} daqiqa, {sekunds} sekund o'tdi ")

#integer24
# days_of_weeks = ['yakshanba', 'dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba']
# kun = int(input("kunni kiriting (1-365 oraliqda): "))
# qoldiq = kun % 7
# print(days_of_weeks[qoldiq])

#integer29
# a = int(input('a = '))
# b = int(input("b = "))
# c = int(input("c = "))

# s_rectangle = a * b
# s_square = c**2
# times_b = b // c
# times_a  = a // c
# total_squares = times_a * times_b
# area_out = s_rectangle - (total_squares * s_square)
# print(f"To'gri to'rtburchakdan qolgan joy {area_out} ga kvadratlar soni esa {total_squares} ga teng")

#integer30 
# given_year = int(input("Yilni kiriting: "))
# age = (given_year // 100) + 1
# print(f"beligan yil {age}-yuz yillika kiradi.")

#interesting
# from datetime import datetime
# date_of_birth= input("Enter  your date of birth like in the following example (day.month.year: 25.12.2002): ")
# day, month, year = date_of_birth.split('.')
# yil = int(year)
# oy = int(month)
# kun = int(day)
# print(datetime(yil, oy , kun))
# print(datetime(yil, oy, kun).strftime("%A"))











