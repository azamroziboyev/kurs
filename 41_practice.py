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

aralash = ['me', 1, 2, 3, 3.5, 2.3, "azam"] 
i = 0
while i < len(aralash):
    item = aralash[i]
    if not isinstance(item, str):
        aralash.remove(i)
    i += 1
print(aralash)
