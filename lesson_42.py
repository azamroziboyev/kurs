from datetime import datetime
def calc_old(name, old):
    """this function calculates the birth year"""
    year = datetime.now().year
    birth_year = year - old
    print(f"{name} {birth_year}-yilda tug'ilgan")

ism = input("what is your name: ")
yosh = int(input("How old are you: "))

calc_old(ism, yosh)


