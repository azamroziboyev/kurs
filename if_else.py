# #if4
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# min_number = a

# if b < min_number and c > b:
#     min_number = b
# elif c <min_number and b > c:
#     min_number = c

# max_number = a

# if b > max_number and c < b:
#     max_number = b
# elif c > max_number and b < c:
#     max_number = c 

# count = max_number - min_number - 2 
# print(count)

#if6
# a = int(input(" a = "))
# b = int(input(" b = "))
# if a>b:
#     print("katta son", a)
# elif b>a:
#     print("katta son", b)
# else:
#     print("ular ikkalasi teng")

#if7
# a = int(input(" a = "))
# b = int(input(" b = "))
# if a<b:
#     print("birinchi")
# else:
#     print("ikkinchi")

#if9
# a = int(input(" a = "))
# b = int(input(" b = "))
# if not a<b:
#     a,b = b,a
# print(a, "va", b)

#if10
# a = int(input(" a = "))
# b = int(input(" b = "))
# if a!=b:
#     a=b=a+b
# else:
#     a=b=0
# print(a,b)

#if11
# a = int(input(" a = "))
# b = int(input(" b = "))
# if a!=b:
#     if a>b:
#         b=a
#     else:
#         a=b
# else:
#     a=b=0
# print(a,b)

#if13
# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))

# min_number = a

# if b < min_number and c > b:
#     min_number = b
# elif c <min_number and b > c:
#     min_number = c

# max_number = a

# if b > max_number and c < b:
#     max_number = b
# elif c > max_number and b < c:
#     max_number = c 
# middle = (max_number + min_number) / 2
# print(middle)

#if14
# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))

# min_number = a

# if b < min_number and c > b:
#     min_number = b
# elif c <min_number and b > c:
#     min_number = c

# max_number = a

# if b > max_number and c < b:
#     max_number = b
# elif c > max_number and b < c:
#     max_number = c 
# if a!=b!=c:
#     if max_number == a  and min_number == b:
#         print(min_number,c,max_number)
#     elif max_number == b and min_number == a:
#         print(min_number,c,max_number)
#     elif max_number == a and min_number == c:
#         print(min_number,b,max_number)
#     elif max_number == c and min_number == a:
#         print(min_number,b,max_number)
#     elif max_number == b and min_number == c:
#         print(min_number,a,max_number)
#     elif max_number == c and min_number == b:
#         print(min_number,a,max_number)

#if15 
# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = "))

# min_number = a

# if b < min_number and c > b:
#     min_number = b
# elif c <min_number and b > c:
#     min_number = c

# max_number = a

# if b > max_number and c < b:
#     max_number = b
# elif c > max_number and b < c:
#     max_number = c 
# if a!=b!=c:
#     if max_number == a  and min_number == b:
#         print(c,max_number)
#     elif max_number == b and min_number == a:
#         print(c,max_number)
#     elif max_number == a and min_number == c:
#         print(b,max_number)
#     elif max_number == c and min_number == a:
#         print(b,max_number)
#     elif max_number == b and min_number == c:
#         print(a,max_number)
#     elif max_number == c and min_number == b:
#         print(a,max_number)  

#if16
# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = ")) 
# if a<b<c:
#     a,b,c= 2*a,2*b,2*c
# else:
#     a,b,c=(-1)*a,(-1)*b,(-1)*c 
# print(a,b,c)

#if17
# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = ")) 
# if a<b<c or a>b>c:
#     a,b,c= 2*a,2*b,2*c
# else:
#     a,b,c=(-1)*a,(-1)*b,(-1)*c 
# print(a,b,c)

#if18
# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = ")) 
# third = a

# if b==c and a!=b:
#     print(f"qolgan bittasining tartib raqami bir son:{a}")
# elif a==c and b!=a:
#     print(f"qolgan bittasining tartib raqami ikki son:{b}")
# elif a==b and c!=a:
#     print(f"qolgan bittasining tartib raqami uch son:{c}")
# else:
#     print("berilgan sonlarning uchtasi ham bir biriga teng yoki ikkitasi o'zaro teng emas")

#if20
# a = int(input(" a = "))
# b = int(input(" b = "))
# c = int(input(" c = ")) 
# distance_ab = int(((a - b)**2)**0.5)
# distance_ac = int(((a - c)**2)**0.5)
# if distance_ab > distance_ac:
#     print("A nuqtaga eng yaqin nuqta C", f"orasidagi masofa esa {distance_ac}")
# if distance_ac > distance_ab:
#     print("A nuqtaga eng yaqin nuqta B", f"orasidagi masofa esa {distance_ab}" )

#if21
# x = int(input("x = "))
# y = int(input("y = "))
# if x==y==0:
#     print(0)
# elif x!=0 and y==0:
#     print(1)
# elif x==0 and y!=0:
#     print(2)
# else:
#     print(3)

#if22
# x = int(input("x = "))
# y = int(input("y = "))
# if x>0 and y>0:
#     print("I chorak")
# elif x<0 and y>0:
#     print("II chorak")
# elif x<0 and y<0:
#     print("III chorak")
# else:
#     print("IV chorak")

#if23
"""shu misoldi ko'rish kerak"""

#if24
# x = int(input("x = "))
# import math
# if x>0:
#     f = 2 * math.sin(x)
# elif x<=0:
#     f = x - 6
# print(f)

#if26
# x = int(input("x = "))
# if x<=0:
#     f = -x
# elif 0<x<2:
#     f = x**2
# elif x>=2:
#     f = 4
# print(f)

#if27
# x = int(input("x = "))


#if28
# year = int(input("yil = "))
# if year < 100:
#     kabisa_yillar_miqdori = year / 4
# total_days = (year * 365) + (kabisa_yillar_miqdori * 1)
# print(total_days)

#if29
# a = int(input("a = "))
# if a%2==0 and a >0:
#     print("musbat juft son")
# elif a%2!=0 and a>0:
#     print("musbat toq son")
# elif a%2==0 and a<0:
#     print("manfiy juft son")
# elif a%2!=0 and a<0:
#     print('manfiy toq son')
# else:
#     print("son nolga teng")

#if30


     



