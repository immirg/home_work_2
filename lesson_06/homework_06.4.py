import random

# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list_of_numbers = [random.randint(1, 100) for _ in range(random.randint(10, 20))]
print(list_of_numbers)

sum_even_num = 0

for i in list_of_numbers:
    if i % 2 == 0:
        sum_even_num += i

print(sum_even_num)
