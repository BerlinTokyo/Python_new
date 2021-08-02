print('Hello world')
name = "ada lovelace"

print(name.title())

print(name.upper())

print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name


print(full_name)

irst_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print("Hello, " + full_name.title() + "!")

#Для включения в текст позиции табуляции используется комбинация символов \t, как в точке (1) :

print("Python")

#Python

print("\tPython")

#. .Python

#Разрывы строк добавляются с помощью комбинации символов \n:

print("Languages:\nPython\nC\nJavaScript")

#Languages:
#Python
#C
#JavaScript

#Следующий пример демонстрирует вывод одного сообщения с разбиением на четыре строки:

print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Languages:
#. .Python
#. .C
#. .JavaScript

favorite_language = 'python '

print(favorite_language)
#'python '

print(favorite_language.rstrip())
#'python'

#Чтобы навсегда исключить пропуск из строки, следует записать усеченное значение обратно в переменную:

avorite_language = 'python '

favorite_language = favorite_language.rstrip()

print(favorite_language)
#'python'

favorite_language = ' python '

print(favorite_language.rstrip())
#' python'

print(avorite_language.lstrip()()
#'python '

print(favorite_language.strip())
#'python'

#str - Строка из символов иначе ошибка
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

#Простой пример списка с названиями моделей велосипедов:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

#В Python также существует специальный синтаксис для обращения к последнему элементу списка. Если запросить элемент с индексом –1, Python всегда возвращает последний элемент в списке:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[-1])