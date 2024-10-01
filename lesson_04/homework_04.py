adventures_of_tom_sawer = """\
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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
tom_sawyer_newlines_replaced: str = adventures_of_tom_sawer.replace('\n', ' ')
print(tom_sawyer_newlines_replaced)
print('* ' * 70)

# task 02 ==
""" Замініть .... на пробіл
"""
tom_sawyer_ellipsis_replaced: str = tom_sawyer_newlines_replaced.replace('....', ' ')
print(tom_sawyer_ellipsis_replaced)
print('* ' * 70)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
tom_sawyer_removing_extra_spaces: str = ' '.join(tom_sawyer_ellipsis_replaced.split())
print(tom_sawyer_removing_extra_spaces)
print('* ' * 70)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
tom_sawyer_count_letter_h_1: int = tom_sawyer_removing_extra_spaces.count('h')
tom_sawyer_count_letter_h_2: int = 0

for word in tom_sawyer_removing_extra_spaces:
    for letter in word:
        if letter == 'h':
            tom_sawyer_count_letter_h_2 += 1

print(f'Буква "h" встерчается в истории {tom_sawyer_count_letter_h_1} раз')
print(f'Буква "h" встерчается в истории {tom_sawyer_count_letter_h_2} раз')
print('* ' * 70)


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
tom_sawyer_count_words_with_capital_letters: int = 0
word_list: list = tom_sawyer_removing_extra_spaces.split()
for word in word_list:
    if word.istitle():
        tom_sawyer_count_words_with_capital_letters += 1

print(f'В тексте присутствует {tom_sawyer_count_words_with_capital_letters} слов с большой буквы')
print('* ' * 70)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
search_word = 'Tom'
len_search_word = len(search_word)
story = tom_sawyer_removing_extra_spaces
len_story = len(story)
count_tom = 0
i = 0 # можно и не объявлять переменную 'i' здесь, но тогда она за пределами цикла 'for' не красиво подсвечивается

for i in range(len_story-len_search_word):
    if story[i:i+len_search_word] == 'Tom':
        count_tom += 1
    if count_tom == 2:
        break

if count_tom < 2:
    print('Том упоменается в тексте меньше двух раз')
else:
    print(f'Второй раз Том встречается в тексте под индексом {i}')
    print(story[i:i+len_search_word])

print('* ' * 70)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawer_sentences
"""
adventures_of_tom_sawer_sentences: list = tom_sawyer_removing_extra_spaces.split('. ')
print(adventures_of_tom_sawer_sentences)
print('* ' * 70)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
word_list: list = tom_sawyer_removing_extra_spaces.split('. ')
tom_sawyer_4th_sentence_lowercase: str = word_list[3].lower()
print(tom_sawyer_4th_sentence_lowercase)
print('* ' * 70)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
word_list: list = tom_sawyer_removing_extra_spaces.split('. ')
sentence_starter_check: bool = False
for sentence in word_list:
    if sentence.startswith('By the time'):
        sentence_starter_check = True
        break
print('Одно из предложений начинается на "By the time"' if sentence_starter_check else 'Ни одно из предложений не '
                                                                                       'начинается на "By the time"')
print('* ' * 70)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
count = 0
count_words_in_last_sentence = len(word_list[len(tom_sawyer_removing_extra_spaces.split('. '))-1].split())
print(f'В последнем предложении рассказа присутствует {count_words_in_last_sentence} слова')

