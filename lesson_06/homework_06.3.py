'''
Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код,
який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. Данні в лісті
можуть бути будь якими
'''

list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = []

for elem in list1:
    if isinstance(elem, str):
        list2.append(elem)

print(list2)
