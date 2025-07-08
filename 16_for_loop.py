"""For loop sikl mavusiga doir masalalar yechimlari"""
#For1
# k = input("k = ")
# n = int(input("n = "))
# print(k*n)

#For2
# a = int(input("a = "))
# b = int(input("b = "))
# count = 0
# for num in range(a, b+1):
#     print(num)
#     count += 1
# print(f"jami ekranga chiqarilgan raqamlar soni {count}")

#For4
# konfet_price = 50000
# for i in range(1, 11):
#     print(f"{konfet_price*i:,}".replace(",", " "))

#For7
# a = int(input("a = "))
# b = int(input("b = "))
# count = 0
# for num in range(a, b+1):
#     count += num
# print(f"{a} dan {b} gacha bo'lgan butun solar yig'indisi {count} ga teng")

#For9
# a = int(input("a = "))
# b = int(input("b = "))
# sum_of_squares = 0
# for i in range(a, b+1):
#     sum_of_squares += i**2
# print(sum_of_squares)

#For10
# n = int(input("n = "))
# s = 0 
# for i in range(1, n+1):
#     s += (1 / i)
# print(round(s,2))

#For11
# n = int(input("Enter n: "))  
# total_sum = 0                
# for k in range(n, 2*n + 1): 
#     total_sum += k ** 2       
# print(total_sum)              

#For12
# n = int(input("n = "))
# total = 0
# for i in range(1, n+1):
#     sign = (-1)**(i + 1)
#     total += sign * (1 + i * 0.1)
# print(f' jami yigindi {round(total, 2)} ga teng')


#For14
# n = int(input("n = "))
# s = 0
# for i in range(1, 2*n,2):
#     s = s +i
# print(s)


#For15
# n = int(input("n = "))
# a = float(input("a = "))
# power = 1
# if n>0:
#     for i in range(1, n+1):
#         power *= a
# else:
#     power = 'please try again later'
# print(power)

#For16
# a = float(input("a = "))
# n = int(input("n = "))

# if n>0:
#     for i in range(1, n+1):
#         print(a ** i)
# else:
#     power = 'please try again later'
#     print(power)


#For17
# a = float(input("a = "))
# n = int(input("n = "))
# sum = 0
# if n>0:
#     for i in range(1, n+1):
#         power = a ** i
#         sum += power
#         print(power)
# else:
#     power = 'please try again later'
#     print(power)
# print(f"Jami darajalar yig;indisi: {int(sum)} ga teng")

#For18
# a = float(input("a = "))
# n = int(input("n = "))
# sum = 1
# for i in range(1, n+1):
#     power = a ** i
#     sum += power * (-1)**i
#     print(power)
# print(f"Jami darajalar yig;indisi: {int(sum)} ga teng")

#For19
# n = int(input("n = "))
# times = 1
# for i in range(1, n + 1):
#     times  *=  i
# print(times)

#For20
# n = int(input("n = "))
# summa = 0
# fact = 1
# for i in range(1, n + 1):
#     fact *= i       
#     summa += fact   
# print("Yig'indi:", summa)

#For21
# n = int(input("n = "))
# summa = 1
# fact = 1
# for i in range(1, n + 1):
#     fact *= i       
#     summa += 1 / fact   
# print("Yig'indi:", summa)


#For22
# x = float(input("x = "))
# n = int(input("n = "))
# summa = 1
# fact = 1
# for i in range(1, n + 1):
#     fact *= i       
#     summa += ((x**i) / fact)   
# print("Yig'indi:", summa)

#For23
# x = float(input("x = "))
# n = int(input("n = "))
# summa = 0
# for i in range(n + 1):
#     power = 2 * i + 1
#     fact = 1
#     for j in range(1, power + 1):
#         fact *= j
#     if i % 2 == 0:
#         term = (x ** power) / fact
#     else:
#         term = - (x ** power) / fact
#     summa += term
# print("Yig'indi:", summa)


#For24
# x = float(input("x = "))
# n = int(input("n = "))
# summa = 0
# for i in range(n + 1):
#     power = 2 * i 
#     fact = 1
#     for j in range(1, power + 1):
#         fact *= j
#     if i % 2 == 0:
#         term = (x ** power) / fact
#     else:
#         term = - (x ** power) / fact
#     summa += term
# print("Yig'indi:", summa)

#For25
# x = float(input("x = "))
# n = int(input("n = "))
# summa = 0
# for i in range(1, n + 1):
#     power = i
#     sign = (-1)**(i - 1)

#     summa += sign * x ** i / i
# print("Yig'indi:", summa)

#For26
# x = float(input("x = "))
# n = int(input("n = "))
# summa = 0
# for i in range(1, n + 1):
#     power = 2*n+1
#     sign = (-1)**i

#     summa += (sign * (x ** power)) / 2 * i + 1
# print("Yig'indi:", summa)

#For27
#For28

#For29
# a = float(input("A = "))
# b = float(input("B = "))
# n = int(input("n = "))

# if not n <= 0:
#     length = b - a
#     segment_size = length / n
#     for i in range(n + 1):
#         point = a + i * segment_size
#         print(point)
# else:
#     print("n butun son emas")


#For30
# import math
# a = float(input("A = "))
# b = float(input("B = "))
# n = int(input("n = "))

# if not n <= 0:
#     length = b - a
#     segment_size = length / n
#     for i in range(n + 1):
#         point = a + i * segment_size
#         f = 1 - math.sin(point)
#         print(point)
#         print(f"f(x) = 1 - sin(x) funksiya qiyamti: {f}")
# else:
#     print("n butun son emas")

"""bu masala"""
#For31
# n = int(input("n = "))
# for i in range(1, n+1):
#     print(f"ketma-ketlikning {i}-hadi {2+1/}")



#For36
# n = int(input("n = "))
# k = int(input("k = "))
# sum = 0
# for i in range(1,n+1):
#     hadi = 1
#     for _ in range(k):
#         hadi  *= i
        
#     sum += hadi
# print(sum)



#For37
# n = int(input("n = "))
# s = 0
# # for i in range(1,n+1):
# #     had = i
# #     for k in range(1,i+1):
# #         had *= had
# #         print(had)
# #     total_had +=had  
# # print(total_had)  

# for i in range(1,n+1):
#     s = i**i + s
# print(s)

#For38
"""bu masalani ko'rish kerak"""
# n = int(input("n = "))
# sum = 0 
# for i in range(0,n+1):
#     if i == 0:
#         sum += 1
#     else:
#         sum += i**(n-i)

#For39
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a+1,b):
#     num = str(i)
#     print(num*i)

"""bu masala"""
#For40
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a+1,b):
#     num = i
#     for marta in range(i+1):
#         print(num)

