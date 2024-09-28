import math

# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on ' \
                      'where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it ' \
                      'doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added ' \
                      'as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
print(alice_in_wonderland)
# task 01 Не совсем понял условие задачи, так как в задании уже проставлены переносы на новую строку в тексте - \n
# task 02 Я так понял что нужно экранировать одинарные кавычки в тексте. Сделал
print('-' * 80)
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436_402
azov_sea_area = 37_800
total_area_of_two_seas = black_sea_area + azov_sea_area
print(f'Общая площадь черного и азовского морей составляет {total_area_of_two_seas} квадратных километров')
print('-' * 80)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_qty_warehouses = 375_291
qty_1st_2nd_warehouses = 250_449
qty_2nd_3rd_warehouses = 222_950

qty_3rd_warehouse = total_qty_warehouses - qty_1st_2nd_warehouses
qty_1st_warehouses = total_qty_warehouses - qty_2nd_3rd_warehouses
qty_2nd_warehouses = total_qty_warehouses - qty_1st_warehouses - qty_3rd_warehouse

print(f'На первом складе {qty_1st_warehouses} товаров, на втором {qty_2nd_warehouses} и на третьем {qty_3rd_warehouse}')
print('-' * 80)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
installment_months = 18
payment_per_month = 1179
computer_cost = installment_months * payment_per_month
print(f'Стоимость компьютера {computer_cost} грн')
print('-' * 80)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print('Остаток от деления 8019 : 8 = ', 8019 % 8)
print('Остаток от деления 9907 : 9 = ', 9907 % 9)
print('Остаток от деления 2789 : 5 = ', 2789 % 5)
print('Остаток от деления 7248 : 6 = ', 7248 % 6)
print('Остаток от деления 7128 : 5 = ', 7128 % 5)
print('Остаток от деления 19224 : 9 = ', 19224 % 9)
print('-' * 80)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
shopping_list = {
    'big pizza': [4, 274],
    'medium pizza': [2, 218],
    'juice': [4, 35],
    'cake': [1, 350],
    'water': [3, 21]
}
big_pizzas = shopping_list['big pizza'][0] * shopping_list['big pizza'][1]
medium_pizzas = shopping_list['medium pizza'][0] * shopping_list['medium pizza'][1]
juice = shopping_list['juice'][0] * shopping_list['juice'][1]
cake = shopping_list['cake'][0] * shopping_list['cake'][1]
water = shopping_list['water'][0] * shopping_list['water'][1]

cost_of_purchases = big_pizzas + medium_pizzas + juice + cake + water
print(f'Для покупки всех продуктов необходимо {cost_of_purchases} грн')
print('-' * 80)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photos_per_page = 8
total_pages = math.ceil(total_photos / photos_per_page)
print(f'Необходимое {total_pages} станиц в альбоме для вклейки фото')
print('-' * 80)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

trip_distance = 1600
fuel_consumption_per_100_km = 9
fuel_tank_capacity = 48

total_fuel_needed = math.ceil(trip_distance / 100 * fuel_consumption_per_100_km)
total_refills = math.ceil(total_fuel_needed/fuel_tank_capacity)

print(f'Для поездки необходимо {total_fuel_needed} литров бензина')
print(f'Необходимо будет сделать {total_refills} заправки по дороге')
