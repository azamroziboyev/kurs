"""For loop sikl mavusiga doir masalalar yechimlari"""
#For1
# k = input("k = ")
# n = int(input("n = "))
# print(k*n)

#For2
# n = int(input("n = "))
# b = int(input("b = "))
# count = 0
# for num in range(n, b+1):
#     print(num)
#     count += 1
# print(f"jami ekranga chiqarilgan raqamlar soni {count}")

#For4
# konfet_price = 50000
# for i in range(1, 11):
#     print(f"{konfet_price*i:,}".replace(",", " "))

#For7
# n = int(input("n = "))
# b = int(input("b = "))
# count = 0
# for num in range(n, b+1):
#     count += num
# print(f"{n} dan {b} gacha bo'lgan butun solar yig'indisi {count} ga teng")

#For9
# n = int(input("n = "))
# b = int(input("b = "))
# sum_of_squares = 0
# for i in range(n, b+1):
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

"""shu misolda ozroq xato bo'lishi mumkin shuning uchun bir qarash kerak"""
#For12
# n = int(input("n = "))
# total = 1
# for i in range(1, n+1):
#     total *= (1 + (i * 0.1))
# print(round(total, 3))


#For13
n = int(input("n = "))
term = 0
for i in range(1, n+1):
    sign = (-1) ** (i + 1)  
    term += sign * (1.0 + i * 0.1)
print(round(term, 2))



