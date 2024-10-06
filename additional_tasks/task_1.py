import pprint
import re

'''
1 - Є 3 группи людей(sets) australia_blacklist, poker_blacklist, alcohol_blacklist.
В кожній групі вказані імена. Вивести тих хто виграв джекпот(є одразу в 3х списках)


2 - Порахувати та вивести(print) кількість букв в строці
Юзер щось вводить(input)
Ваша задача надрукувати кількість кожного символу того що він ввів.
Прикдад:
Юзер вводить:
My name is Emmy Santiago.
ВИ прінтаете щось накшталт:
M = 1, y = 2, n = 2, ...(або в іншому форматі, це не принциповоб головне, що б чітко було зрозуміло скільки разів зустрічаеться кожна буква)

Тобто кожну букву та скільки разів вона зустрічаеться
Підказка: це про словники, get можна використати для тотго щоб витягнути чи є ключ без помилки та надати дефолтне значення

3 - Вирішити задачу 2 без словника за 2 строки:
1 строка це input
2 строка це рішення
'''

# task 1
australia_blacklist = {"John Smith", "Emily Davis", "Michael Johnson", "Sophia Brown", "David Wilson", "Jack Miller"}
poker_blacklist = {"Emily Davis", "David Wilson", "Isabella Clark", "Michael Johnson", "Jack Miller", "Liam Evans"}
alcohol_blacklist = {"Michael Johnson", "David Wilson", "Jack Miller", "Olivia Martin", "Lucas Taylor"}

jackpot = set(australia_blacklist).intersection(set(poker_blacklist).intersection(alcohol_blacklist))
print(jackpot)

# task 2
word = (re.sub(r'[^\w]', '', input('>>> ').lower()))

pprint.pprint(dict(set((i, word.count(i)) for i in word)))

# task 3
word = input('>>> ').replace(' ', '').replace(' ', '').replace(',', '').replace('.', '').lower()
pprint.pprint(set((i, word.count(i)) for i in word))
