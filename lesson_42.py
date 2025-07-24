# from datetime import datetime
# def calc_old(name, old):
#     """this function calculates the birth year"""
#     year = datetime.now().year
#     birth_year = year - old
#     print(f"{name} {birth_year}-yilda tug'ilgan")
#
# ism = input("what is your name: ")
# yosh = int(input("How old are you: "))
#
# calc_old(ism, yosh)




# def make_power(raqam):
#     raqam_kubi = raqam ** 3
#     raqam_kvadrat = raqam ** 2
#     return raqam_kvadrat, raqam_kubi
#
# number = int(input("butun son kiriting: "))
# print(f"raqm kubi: {make_power(number)[1]}\n"
#       f"raqam kvadrati: {make_power(number)[0]}")


"""amlaiyot 3-inchi"""
# def get_type(number):
#     if number%2==0:
#         return "raqam juft"
#     else:
#         return "raqam toq"
#
# raqam = int(input("Raqamni kiriting men sizga uning toq yoki juftligini aytaman: "))
# print(get_type(raqam))

"""5-masla"""
# def make_power(x, y):
#     return x**y
#
# x = int(input("x: "))
# y = int(input("y: "))
# print(make_power(x,y))

"""6-masala"""
# def make_power(x, y=2):
#     return int(x) ** int(y)
#
# x = input("x: ")
# y = input("y (press Enter to use default 2): ")
#
# if y == "":
#     print(make_power(x))
# else:
#     print(make_power(x, y))

# """7-masala"""
# def bolish_alomatlari(num):
#     for i in range(1,11):
#         if num%i==0:
#             print( f"{num} soni {i} ga qoldiqsiz bo'linadi")
# raqam = int(input("Bitta son kiriting 10 dan katta: "))
# bolish_alomatlari(raqam)



