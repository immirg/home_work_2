import pprint

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    """
    print multiplication table for given number
    :param number: given number
    """
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_second_num(a, b):
    """
    calculating the sum of two given numbers
    :param a: first number
    :param b: second number
    :return: the result of adding two numbers
    """
    return a + b


print(sum_second_num(a=3, b=4))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average_num(numbers: list):
    """
    finding the average number from a given list of numbers
    :param numbers: a list of numbers in which needed to find the arithmetic mean
    :return: found arithmetic mean
    """
    return round(sum(numbers)/len(numbers), 2)


print(average_num(numbers=[4, 8, 6, 5, 3, 2]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_letters(words: str):
    """
    reverses the order of letters in a given string
    :param words: given string
    :return: a new line in which the order of letters is changed from last to first
    """
    return words[::-1]


def reverse_words(sentence: str):
    """
    replacing words in reverse order in a sentence
    :param sentence: given string
    :return: a new line in which the word order is reversed
    """
    return sentence.split()[::-1]


print(reverse_letters('Написати функцію, яка приймає рядок та повертає його у зворотному порядку.'))
print(reverse_words('Написати функцію, яка приймає рядок та повертає його у зворотному порядку.'))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def find_the_long_word(word_list: list):
    """
    find the longest word in a given list of words
    :param word_list: given list of words
    :return: the first long word found from the list
    """
    len_word = 0
    index = 0
    for ind, word in enumerate(word_list):
        if len(word) > len_word:
            len_word = len(word)
            index = ind
    return word_list[index]


sentence = 'Написати функцію, яка приймає список слів та повертає найдовше слово у списку.'
remove_non_letters = ''.join(elem for elem in sentence if elem.isalpha() or elem == ' ')
list_of_words = remove_non_letters.split()
print(find_the_long_word(list_of_words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    """
    check if the second line is in the first line
    :param str1: the first line in which the search for the second line occurs
    :param str2: the second line to be searched for in the first line
    :return: index from which the second line in the first line begins if it is present there, otherwise -1 is returned
    """
    len_str1 = len(str1)
    len_str2 = len(str2)
    if str2 in str1:
        for i in range(len_str1):
            if str1[i:i+len_str2] == str2:
                return i
    return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}


def search_for_cars_by_criteria(*search_criteria):
    """
    search for the first 5 cars by specified criteria
    :param search_criteria: parameters by which needed to search for suitable cars
    :return: call the following function to sort the found cars by price
    """
    found_cars = []
    for car in car_data:
        if search_criteria[0] <= car_data[car][1] and search_criteria[1] <= car_data[car][2] and search_criteria[2] >= car_data[car][4]:
            if len(found_cars) < 5:
                found_cars.append([car, car_data[car]])
    return sort_cars_by_price(found_cars)


def sort_cars_by_price(found_cars):
    """
    sorting found cars by price in ascending order
    :param found_cars: list of cars that need to be sorted by price
    :return: call the function to print found cars into the console
    """
    len_found_cars = len(found_cars)
    if len(found_cars) >= 2:
        for _ in range(len_found_cars-1):
            for line in range(len_found_cars-1):
                if found_cars[line][1][4] > found_cars[line+1][1][4]:
                    found_cars[line], found_cars[line+1] = found_cars[line+1], found_cars[line]
    return print_results(found_cars)


def print_results(found_cars):
    """
    print output into the console of found cars
    :param found_cars: found cars that should be printed into the console
    """
    if len(found_cars) >= 1:
        print('По заданным критерием было найдены следующие машины:')
        pprint.pprint(found_cars)
    else:
        print('По заданным критериям не было найдено ни одной машины')


search_for_cars_by_criteria(2017, 1.6, 36000)

# task 8
adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""


def replace_paragraph_with_space(adventures_of_tom_sawyer):
    """
    replace paragraph line with space
    :param adventures_of_tom_sawyer: original story format
    :return: move to next function to remove ellipses in text
    """
    tom_sawyer_newlines_replaced: str = adventures_of_tom_sawyer.replace('\n', ' ')
    return replacing_an_ellipsis_with_a_space(tom_sawyer_newlines_replaced)


# task 9


def replacing_an_ellipsis_with_a_space(tom_sawyer_newlines_replaced):
    """
    replacing an ellipsis with a space
    :param tom_sawyer_newlines_replaced: original story format
    :return: move to next function to remove extra spaces
    """
    tom_sawyer_ellipsis_replaced: str = tom_sawyer_newlines_replaced.replace('....', ' ')
    return removing_extra_spaces(tom_sawyer_ellipsis_replaced)


# task 10


def removing_extra_spaces(tom_sawyer_ellipsis_replaced):
    """
    removing extra spaces
    :param tom_sawyer_ellipsis_replaced: original story format
    :return: corrected history
    """
    tom_sawyer_removing_extra_spaces: str = ' '.join(tom_sawyer_ellipsis_replaced.split())
    return tom_sawyer_removing_extra_spaces


print(replace_paragraph_with_space(adventures_of_tom_sawyer))


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
