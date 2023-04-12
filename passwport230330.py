from random import choice, randint, shuffle

# если хотите, чтобы пароли копировались в буфер обмена, необходимо
# установить библиотеку pyperclip:
# pip install pyperclip
#
# для x11 нужно ещё дополнительно поставить xsel, например в linux:
# sudo apt-get install xsel
#
# если не хотите, чтобы пароли копировались в буфер обмена,
# нужно поставить символ решётка перед следующей строкой:
# from pyperclip import copy

from pyperclip import copy

l = 'adefmqrt'
L = 'AEFHJLNR'
d = '2347'
s = '+-_*&$#?=@<>'

print("""Генератор паролей ХОРОШО РАЗЛИЧАЕМЫХ символов v3.3.30 (c) Vitaly Portunov, 2023\n
Не генерит похожих символов, таких, как Il15Ss9guvb6GDQ0OWwСсKkB8ij и спецсимволов: ;:,.'
В пароле присутствуют заглавные и строчные латинские буквы, одна цифра и один спецсимвол.\n
Сгенерированные пароли копируются в буфер обмена.\n""")

first, lP = 1, 8
while 1970:
    if first:
        first, nP = 0, 1
    else:
        inp = input('\nСколько ещё нужно паролей? (Enter - для выхода): ')
        if inp.isdigit():
            nP = int(inp)
        else:
            break
    while 1970:
        passwords = ''
        print('Длина пароля [', lP, '] (4..80): ', sep='', end='')
        inp = input()
        if inp.isdigit():
            lP = int(inp)
        if 3 < lP < 81:
            break
    for n in range(nP):
        password = choice(d) # добавляем одну цифру
        password += choice(s) # добавляем один спецсимвол
        for i in range(randint(1, lP-3)): 
            password += choice(l) # добавляем строчные
        for i in range(lP - len(password)):
            password += choice(L) # добавляем заглавные
            
        # перемешиваем сгенерированные символы для большей стойкости пароля
        password_list = list(password)
        shuffle(password_list)
        password = ''
        for ch in password_list:
            password += ch

        passwords += password + '\n' # формируем пароли, разделяя переводом строки
    passwords = passwords[:-1]
    
    # если не хотите, чтобы пароли копировались в буфер обмена,
    # нужно поставить символ решётка перед следующей строкой: # copy(passwords)
    copy(passwords)
    
    print(passwords)
