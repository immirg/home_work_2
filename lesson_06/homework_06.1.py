'''
Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()
'''

words = input('>>> ')

splitting_line_into_letters = [i for i in words if i != ' ']
set_letters = set(splitting_line_into_letters)

if len(set_letters) > 10:
    print(True)
else:
    print(False)
