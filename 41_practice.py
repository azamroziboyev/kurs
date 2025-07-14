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

"""gegegegegegeggegegeegegeggegg """

order = 0
order_list = {}
total_price = []
while True:
    order_name = input("Nima buyurasiz?:\n")
    if order_name=="exit" or order_name == "Exit":
        break
    price = int(input("narxini kiriting: "))
    total_price.append(price)
    order_list[order_name] = price

ready_orders = [f"{k:<15} {v:,} so'm" for k, v in order_list.items()]
ready_orders_text = "\n".join(ready_orders)

doc = f"""
===========================================
            Buyurtmalaringiz!
===========================================
{ready_orders_text}    
-------------------------------------------
Jami:           {sum(total_price):,} so'm
===========================================
buyurtma uchun raqam: (998) 99 999 99 99
"""
print(doc)       