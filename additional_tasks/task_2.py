'''
1) Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'
'''


def palindrome_check(word):
    """
    check the entered word for a palindrome
    :param word: word that should be checked for palindrome
    if the entered word is a palindrome then '+' is printed otherwise '-'
    """
    print('+' if word == word[::-1] else '-')


word = input('>>> ')
palindrome_check(word=word)

'''
2) Написати валідатор для пошти. Користувач вводить пошту, а програма повинна перевірити:
- в адресі є тільки 1 '@', після '@' йде тільки 1 '.'
Не використовувати RE
Якщо умови виконані, то вивести "пошта валідна", інкше вивести "пошта не валідна"
'''


def check_email(email):
    """
    checking email for correctness
    :param email: incoming email for verification
    :return: if the email is correct it returns 'Mail is valid' otherwise 'Mail is not valid'
    """
    at_count = email.count('@')
    if at_count != 1:
        return 'Mail is not valid'
    at_id = email.find('@')
    domain_part = email[at_id:]
    if domain_part.count('.') == 1:
        return 'Mail is valid'
    return 'Mail is not valid'


email = input('>>> ')
print(check_email(email))

'''
3) Додати перевірку введеної IP-адреси. Адреса вважається коректно заданою, якщо вона:
складається з 4 чисел (а не літер чи інших символів)
числа розділені точкою
кожне число в діапазоні від 0 до 255 Якщо адреса неправильна, виводьте повідомлення: «Неправильна IP-адреса». 
Повідомлення "Неправильна IP-адреса" має виводитися лише один раз, навіть якщо кілька пунктів вище не виконані.
'''


def check_ip(ip: str):
    """
    check that the IP address consists of 4 numbers in the range from 0 to 255 and the numbers are separated by a dot
    :param ip: IP for verification
    :return: If the address is correct 'Correct IP address' otherwise 'Incorrect IP address'
    """
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for elem in ip:
        if elem not in symbols:
            return 'Incorrect IP address'
    list_ip = [int(i) for i in ip.split('.')]
    if ip.count('.') != 3 or len(list_ip) != 4:
        return 'Incorrect IP address'
    for i in list_ip:
        if i > 255:
            return 'Incorrect IP address'
    return 'Correct IP address'


ip = '17.172.224.47'
print(check_ip(ip))
