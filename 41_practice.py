# """Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro`yxatga joylang."""
# order = 0
# order_list = []
# while not (order=='exit' or order == 'Exit'):
#     order = input("Nima buyurasiz?:\n")
#     order_list.append(order,)
# ready_orders = "\n" .join(order_list)

# doc = f"""
# ===========================================
#             Buyurtmalaringiz!
# ===========================================
# {ready_orders}
# ===========================================
# buyurtma uchun raqam: (998) 99 999 99 99
# """
# print(doc)

"""e-commerce """ 

# order = 0
# order_list = {}
# total_price = []
# while True:
#     order_name = input("Nima buyurasiz?:\n")
#     if order_name=="exit" or order_name == "Exit":
#         break
#     price = int(input("narxini kiriting: "))
#     total_price.append(price)
#     order_list[order_name] = price

# ready_orders = [f"{k:<15} {v:,} so'm" for k, v in order_list.items()]
# ready_orders_text = "\n".join(ready_orders)

# doc = f"""
# ===========================================
#             Buyurtmalaringiz!
# ===========================================
# {ready_orders_text}    
# -------------------------------------------
# Jami:           {sum(total_price):,} so'm
# ===========================================
# buyurtma uchun raqam: (998) 99 999 99 99
# """
# print(doc)

"""Bizda “aralash” nomli ro`yxat mavjud. O`z nomidan kelib-chiqgan holda ro`yxat tarkibida int, str, 
float kabi har turdagi ma’lumotlar mavjud. while tsikli yordamida ro`yxatda faqat bir turdagi 
(misol uchun faqat str turidagi) ma’lumotlar qolsin, qolganlari yo`qolsin. Yakunda tahrirlangan 
ro`yxatni ko`rsatsin. 
"""

# aralash = ['me', 1, 2, 3, 3.5, 2.3, "azam"] 
# i = 0
# while i < len(aralash):
#     item = aralash[i]
#     if not isinstance(item, str):
#         aralash.pop(i)
#     else:
#         i += 1
# print(aralash)




"""1 dan n gacha bo`lgan sonlar orasida a ga ham, b ga ham bo`linmaydigan sonlar nechtaligini topuvchi dastur tuzing.
Bunda n va a va b lar foydalanuvchi tomonidan kiritiladi.
Izoh: a va b sonlari tub sonlar va ular n dan kichik bo`ladi.
"""
# n = int(input(" n sonini kiriting:\n"))
# a = int(input(" a tub sonini kiriting: \n"))
# b = int(input(" b tub sonini kiriting\n"))
# if a>b:
#     i=a
# else:
#     i=b
# bulinmaydiganlar = 0
# while i < n:
#     if not i%a==0 and not i%b==0:
#         bulinmaydiganlar += 1
#         print(i)
#     i += 1
# print(bulinmaydiganlar)


"""while tsikli yordamida mukammal sonlar ro`yxatini yarating. Mukammal sonlar 
– o`zidan tashqari barcha bo`luvchilari yig`indisiga teng bo`lgan sonlardir. Misol uchun:
6 = 1 + 2 + 3
"""
# perfect_numbers = []
# n = 2

# while n <= 10000:
#     dividers = []
#     i = 1
#     while i < n:
#         if n % i == 0:
#             dividers.append(i)
#         i += 1
#     if sum(dividers) == n:
#         perfect_numbers.append(n)
#     n += 1

# print("Perfect numbers up to 10000:", perfect_numbers)

# """ while sikli yordamida so'zlarni yodlash dasturi"""
# words = {}
# i = 1
# while i < 7:
#     word_eng = input(f"{i}-inglizcha so`zni kiriting (yakunlash uchun “tamom” so`zini kiriting.): ")
#     if word_eng=='tamom':
#         break
#     word_uz = input(f"{word_eng} so`zining o`zbekcha tarjimasini kiriting: ")
#     words[word_eng] =  word_uz
#     i += 1 
# print("Diqqat, sinovni boshlaymiz...")
# c = 0
# correct_answers = []
# wrong_answers = []
# while c < len(words):
#     keys = list(words.keys())

#     answer = input(f"{keys[c]}- ")
   

#     if answer == words[keys[c]]:
#         correct_answers.append(answer)
#     else:
#         wrong_answers.append(answer)
#     c += 1


# result_page = f"""
# ======================================
#              Results
# ======================================
# to'gri javoblar soni:{len(correct_answers)}
# to'gri javoboblar:{correct_answers}

# noto'g'ri javoblar soni:{len(wrong_answers)}
# noto'gri javoblar: {wrong_answers}
# ======================================
# """ 

# print(result_page)


""" Foydalanuvchidan n ning qiymatini qabul qilib olib, ushbu qonuniyatga mos keluvchi qiymatni hisoblang. Albatta while tsikli yordamida.
"""
# n = int(input("n = "))
# s = 1
# i = 1
# while True:
#     s += 1/(n)**n
#     i += 1
#     if i >= n:
#         break
# print(s)




















from itertools import islice
sl = islice("123456", 2)
print(list(sl))


