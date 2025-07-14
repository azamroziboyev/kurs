
#While1
# a = int(input("a = "))
# b = int(input("b = "))
# sum = 0
# while sum < a:
#     sum += b
# print(sum)
# print(f"here is the difference:{sum - a}")


#while2
# a = int(input("a = "))
# b = int(input("b = "))
# sum = 0
# count = 0
# while sum < a:
#     sum += b
#     count += 1
#     if (sum + b)>a:
#         break
# print(f"A kesmada B kesmani {count} marta joylashtirish mumkin")

#while3
# n = int(input("n = "))
# k = int(input("k = "))
# sum = 0
# count = 0
# while (sum + k) <= n:
#     sum += k
#     count += 1
    
# print(f"N sonini K soniga bo'lgandagi qoldiq {n - sum}\nbutun qismi esa {count} ga teng")

#while4
# n = int(input("n = "))
# sum = 0
# count = 0
# while sum < n:
#     sum += 3
#     count += 1
# if sum==n:
#     print("3-ning darajasi")
# else:
#     print("3-ning darajasi emas")


#while5
# n = int(input("n = "))
# sum = 1
# count = 0
# while sum < n:
#     sum *= 2
#     count += 1
# print(count)


#while6
# n = int(input("n = "))
# sum = 1
# count = 0
# while n > 0:
#     sum = sum*n
#     n = n-2
# print(sum)

#while7
# n = int(input("n = "))
# sum = 1
# a = 1
# while a < n:
#     sum = sum + 1
#     a = sum ** 2
# print(sum)

#while8 
# n = int(input(" n = "))
# sum = 1
# a = 1
# while  not a > n:
#     sum = n - 1
#     a = sum **2
# print(sum)

#while12
# n = int(input("n = "))
# sum = 0
# k = 0
# while sum <= n:
#     if sum + k > n:
#         break
#     k += 1
#     sum = sum + k
# print(k)

#while13
# n = int(input("n = "))
# sum = 1
# k = 1
# while not sum >= n:
#     k += 1
#     sum = sum + 1/k
# print(k)

#while 15
# s = int(input("summa: "))
# p = int(input("foiz: "))
# months = 0
# target = 2*s
# while s < target:
#     months += 1
#     s += s*p/100
# print(months)

#while 16
# from datetime import datetime
# now = datetime.now()
# p = int(input("foiz: "))
# distance = 10
# days = 0
# while distance < 200:
#     days += 1
#     distance += distance*p/100
# doc = f"""
# ====================================================
#              Sportsmenning kundaligi
# ====================================================
# maqsad:200 km masofaga yugurish.

# kunlik foizlar: {p}

# jami masofa: {distance} 

# Yugurilgan kunlar miqdori: {days}
                      
#                                date: {now.strftime("%d.%m.%Y")}
#                                       {now.strftime("%H:%M:%S")}
# ====================================================

# """
# print(doc)

#while 17
n = int(input("n = "))
m = int(input("m = "))
sum = 0 
count = 0

