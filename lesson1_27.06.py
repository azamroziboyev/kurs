
""" 4- bo'limdagi masalalarning javoblari """
#begin3
# a = int(input("a = "))
# b = int(input("b = "))

# s = a * b 
# p = 2 * (a + b)
# print(f"tomonlari {a} va {b}  bo'lgan to'g'ri to'rtbburchakning suzasi {s} ga Perimetri {p} ga teng ")


#begin4
# d = int(input("d = "))
# pi = 3.14
# l = pi * d
# print(f"tomoni {d} bo'lgan aylananing uzunligi {l} ga teng")

#begin5
# a = int(input("a = "))
# v = a**3
# s = 6 * a**2
# print(f"tomoni {a} ga teng bo'lgan kubning  hajmi {v} ga to'la sirti {s} ga teng")

#begin6
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# v = a * b * c
# s = 2 * (a*b + b*c + a*c)
# print(f"tomonlari {a,b,c} bo'lgan parallipipedning hajmi {v} ga to'la sirti {s} ga teng ")

#begin9
# try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     kop = a * b
#     ildiz = kop**(1/2)
#     if kop > 0:
#         print(f"ikkita {a} va {b} musbat sonning o'rta geometrigi {ildiz} ga teng")
#     else:
#         print("Iltimos musbat sonalrni kiriting")
# except ValueError:
#     print("ilitmos faqat raqamlardan foydalaning")

#begin11
# a = int(input("a = "))
# b = int(input("b = "))
# sum = a + b
# kop = a * b
# mod_a = int((a**2)**(1/2))
# mod_b = int((b**2)**(1/2))
# print(f"nolga teng bo'lmagan ikkita {a} va {b} sonlarning yig'indisi {sum} ga ko'paytmasi {kop} ga, modullari mos ravishda {mod_a} va {mod_b} ga teng ")
    
#begin12
# a = int(input("a = "))
# b = int(input("b = "))
# c = int((a**2 + b**2)**(1/2))
# p = a + b + c
# print("tomonlari", a ,  "va", b,  "ga teng bo'lgan uchburchakning gipotenuzasi", c, " ga  Perimetri esa", p,  "ga teng" )

#begin16
# x = int(input("x = "))
# y = int(input("y = "))
# print(f"orasidagi masofa {((x-y)**2)**(1/2)}")

#begin17
# a = int(input("a = "))
# b = int(input("b = "))
# ac = ((a - c)**2)**(1/2)
# bc = ((b - c)**2)**(1/2)
# print(f"berilgan {a,b,c} nuqtalarning ac va bc kesmalari mos ravishda {ac} va {bc} ga teng")

#begin20
# x = int(input("x1 = "))
# y = int(input("y1 = "))
# a = int(input("x2 = "))
# b = int(input("y2 = "))
# result = ((a-x)**2 (b-y)**2)**(1/2)
# print("berilgan ikki nuqta orasidagi masofa", result)

#begin23
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# a,b,c = b,c,a
# print(f'yangilangan  qiymatlar: {a,b,c}')

#begin25
# x =int(input("x = "))
# y = 3 * (x**6) - 6 * (x**2) - 7
# print(f"funksiyaning qiymati: {y}")

#begin27
# a = int(input("a = "))
# print(f"{a} sonining 2,4,8 darajalari mos ravishda {a**2, a**4, a**8} ga teng")

#begin29
# gradus = int(input("gradusni kiriting: "))
# pi = 3.14
# radian = gradus*pi/180
# print(f"berilgan {gradus}ning radian shakli {radian} ga teng")

#begin31
# temp_farangeyt = int(input('Temperatura Farangeyt shkalasida: '))
# temp_selsiy = int((temp_farangeyt - 32)*5/9)
# print(f"berilgan farangeyt shkalasidagi harorat selsiyda  {temp_selsiy}gradusga teng")

#begin32
# temp_selsiy = int(input('Temperatura selsiy shkalasida: '))
# temp_farangeyt = int((9*temp_selsiy/5)+32)
# print(f"berilgan selsiy shkalasidagi harorat selsiyda  {temp_farangeyt} frangeytga teng")

#begin34
# konfet_narxi = int(input("konfet narxi: "))
# konfet_massa = int(input("konfet massasini kiriting: "))
# shokolad_narxi = int(input("shokolad narxi: "))
# shokolad_massa = int(input("shokolad massasini kiriting: "))

# shokolad_narx_kg = int(shokolad_narxi / shokolad_massa)
# konfet_narx_kg = int(konfet_narxi / konfet_massa)


# if konfet_narx_kg > shokolad_narx_kg:
#     farq = konfet_narx_kg - shokolad_narx_kg
#     print(f"konfet shokoladdan {farq} so'mga qimmat!")
# elif konfet_narx_kg <  shokolad_narx_kg:
#     farq = shokolad_narx_kg - konfet_narx_kg
#     print(f"shokolad konfetdan {farq} so'mga qimmat!")
# else:
#     print("shokolad va konfetning narxi bir xil")

#begin35
