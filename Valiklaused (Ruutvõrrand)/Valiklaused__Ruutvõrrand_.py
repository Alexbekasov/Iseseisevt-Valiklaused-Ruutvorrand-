# Ulesanne 1

number = int(input("Введите число: "))


if number > 0:
    print("Число положительное")
    
    
    
    if number % 2 == 0:
        print("Число четное")
    else:
        print("Число нечетное")
elif number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# Ulesanne 2

nurk1 = int(input("Введите первый угол треугольника: "))
nurk2 = int(input("Введите второй угол треугольника: "))
nurk3 = int(input("Введите третий угол треугольника: "))

if nurk1 > 0 and nurk2 > 0 and nurk3 > 0:
    if nurk1 + nurk2 + nurk3 == 180:
        print("Сумма углов получилась 180! Это треугольник! Сейчас я вам скажу, какой именно.....")
        
       
        if nurk1 == nurk2 == nurk3:
            print("Треугольник равносторонний.")
        elif nurk1 == nurk2 or nurk2 == nurk3 or nurk1 == nurk3:
            print("Треугольник равнобедренный.")
        else:
            print("Треугольник разносторонний.")
    else:
        print("Сумма углов не равна 180, это не может быть треугольником.")
else:
    print("Все углы должны быть положительными числами.")

# Ulesanne 3

vastus = input("Kas soovite teada nädalapäeva järgi järjestusnumbrist? (jah/ei): ").strip().lower()

if vastus == "jah":
    
    paev = int(input("Sisestage nädalapäeva number (1 kuni 7): "))
    
    
    if 1 <= paev <= 7:
        
        if paev == 1:
            print("Esmaspäev")
        elif paev == 2:
            print("Teisipäev")
        elif paev == 3:
            print("Kolmapäev")
        elif paev == 4:
            print("Neljapäev")
        elif paev == 5:
            print("Reede")
        elif paev == 6:
            print("Laupäev")
        elif paev == 7:
            print("Pühapäev")
    else:
        print("Vale päevanumber. Sisestage number vahemikus 1 kuni 7.")
else:
    print("Te ei soovi teada nädalapäeva nime.")


# Ulesanne 4

day = int(input("Введите день рождения: "))  
month = int(input("Введите месяц рождения: "))  

if month == 1 and day >= 20 or month == 2 and day <= 18:  
    print("Ваш знак зодиака: Водолей")  
elif month == 2 and day >= 19 or month == 3 and day <= 20:  
    print("Ваш знак зодиака: Рыбы")  
elif month == 3 and day >= 21 or month == 4 and day <= 19:  
    print("Ваш знак зодиака: Овен")  
elif month == 4 and day >= 20 or month == 5 and day <= 20:  
    print("Ваш знак зодиака: Телец")  
elif month == 5 and day >= 21 or month == 6 and day <= 20:  
    print("Ваш знак зодиака: Близнецы")  
elif month == 6 and day >= 21 or month == 7 and day <= 22:  
    print("Ваш знак зодиака: Рак")  
elif month == 7 and day >= 23 or month == 8 and day <= 22:  
    print("Ваш знак зодиака: Лев")  
elif month == 8 and day >= 23 or month == 9 and day <= 22:  
    print("Ваш знак зодиака: Дева")  
elif month == 9 and day >= 23 or month == 10 and day <= 22:  
    print("Ваш знак зодиака: Весы")  
elif month == 10 and day >= 23 or month == 11 and day <= 21:  
    print("Ваш знак зодиака: Скорпион")  
elif month == 11 and day >= 22 or month == 12 and day <= 21:  
    print("Ваш знак зодиака: Стрелец")  
else:  
    print("Ваш знак зодиака: Козерог") 


# Ulesanne 5


value = input("Palun kirjuta mulle midagi :) ")  

if value.isdigit():  
    num = int(value)  
    print("Это целое число. 50% от него:", num // 2)  

elif value.replace(".", "", 1).isdigit():  
    num = float(value)  
    print("Это дробное число. 70% от него:", num * 0.7)  

else:  
    print("Это текст:", value) 
 
# Ulesanne 6

import math

answer = input("Решить квадратное уравнение? (да/нет): ")

while answer != "да":
    answer = input("Решить квадратное уравнение? (да/нет): ")

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

D = b * b - 4 * a * c
print("Дискриминант:", D)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Корни:", round(x1, 2), "и", round(x2, 2))
elif D == 0:
    x = -b / (2 * a)
    print("Один корень:", round(x, 2))
else:
    print("Нету корней")


