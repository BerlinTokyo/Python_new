alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#В словаре alien_0 хранятся два атрибута: цвет (color) и количество очков (points).
#Следующие две команды print читают эту информацию из словаря и выводят ее на экран:
#green
#5

#В Python словарь заключается в фигурные скобки {}, в которых приводится последовательность пар «ключ—значение», как в предыдущем примере:

#Добавление новых пар «ключ—значение»
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0 #Вот такая конструкция добавления
alien_0['y_position'] = 25
print(alien_0)
#Обратите внимание: порядок пар «ключ—значение» не соответствует порядку их добавления.

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow' #Изменение значений в словаре
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Пришелец перемещается вправо.
# Вычисляем величину смещения на основании текущей скорости.
if alien_0['speed'] == 'slow':
 x_increment = 1
elif alien_0['speed'] == 'medium':
 x_increment = 2
else:
 # Пришелец двигается быстро.
 x_increment = 3
# Новая позиция равна сумме старой позиции и приращения.
alien_0['x_position'] = alien_0['x_position'] + x_increment #Изменение значений в словаре
print("New x-position: " + str(alien_0['x_position']))

#Удаление пар «ключ—значение»
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points'] #Конструкция удаления
print(alien_0)

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 } #Можно еще делать так
print("Sarah's favorite language is " + favorite_languages['sarah'].title() +  ".")

men = {'first_name' : 'devid', 'last_name' : 'stupid', 'age' : 19, 'city' : 'zalupa'}
print(men['first_name'] + '    ' + men['last_name'] + '   ' + str(men['age']) + '   ' + men['city']) #Все работает)


#Но что если вы хотите просмотреть все данные из словаря этого пользователя? Для этого можно воспользоваться перебором в цикле for:
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
for key, value in user_0.items(): #создание имен для ключей и значений
 print("\nKey: " + key)
 print("Value: " + value)
#чтобы написать цикл for для словаря, необходимо создать имена для двух переменных, в которых будет храниться ключ и значение из каждой пары «ключ—значение». Этим двум переменным можно присвоить любые имена — с короткими однобуквенными именами код будет работать точно так же: for k, v in user_0.items()

#Перебор всех ключей в словаре Метод keys() удобен в тех случаях, когда вы не собираетесь работать со всеми значениями в словаре. Переберем словарь favorite_languages и выведем имена всех людей, участвовавших в опросе:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys(): #keys
 print(name.title()) 
#На самом деле перебор ключей используется по умолчанию при переборе словаря, так что этот код будет работать точно так же, как если бы вы написали for name in favorite_languages:

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
 print(name.title())

if name in friends:
 print(" Hi " + name.title() +
 ", I see your favorite language is " + favorite_languages[name].title() + "!")
#В точке  строится список друзей, для которых должно выводиться сообщение. В цикле выводится имя очередного участника опроса, а затем в точке  программа проверяет, входит ли текущее имя в список друзей. Если имя входит в список, выводится специальное приветствие с упоминанием выбранного языка. Чтобы получить язык в точке , мы используем имя словаря и текущее значение name как ключ. Имя выводится для всех участников, но только друзья получают еще и специальное сообщение

#Метод keys() также может использоваться для проверки того, участвовал ли конкретный человек в опросе:
if 'erin' not in favorite_languages.keys():
 print("Erin, please take our poll!")

#Для получения упорядоченной копии ключей можно воспользоваться функцией sorted():
for name in sorted(favorite_languages.keys()):
 print(name.title() + ", thank you for taking the poll.")

#Если вас прежде всего интересуют значения, содержащиеся в словаре, используйте метод values() для получения списка значений без ключей.
print("The following languages have been mentioned:")
for language in favorite_languages.values():
 print(language.title())

#Для небольших словарей это может быть приемлемо, но в опросах с большим количеством респондентов список будет содержать слишком много дубликатов. Чтобы получить список выбранных языков без повторений, можно воспользоваться множеством (set).
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): #set
 print(language.title())


#Вложение
#Иногда нужно сохранить множество словарей в списке или сохранить список как значение элемента словаря. Создание сложных структур такого рода называется вложением. Вы можете вложить множество словарей в список, список элементов в словарь или даже словарь внутрь другого словаря. Как наглядно показывают следующие примеры, вложение — чрезвычайно мощный механизм.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)

# Создание пустого списка для хранения пришельцев.
aliens = []
# Создание 30 зеленых пришельцев.
for alien_number in range(30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)

# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
 print(alien)
print("...")
# Вывод количества созданных пришельцев.
print("Total number of aliens: " + str(len(aliens)))

#Например, чтобы превратить первых трех пришельцев в желтых, двигающихся со средней скоростью и приносящих игроку по 10 очков, можно действовать так:
for alien in aliens[0:3]:
 if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10

# Вывод первых 5 пришельцев:
for alien in aliens[0:5]:
 print(alien)
print("...")

#Цикл можно расширить, добавив блок elif для превращения желтых пришельцев в красных — быстрых и приносящих игроку по 15 очков. Мы не станем приводить весь код, а цикл выглядит так:
for alien in aliens[0:3]:
 if alien['color'] == 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10
 elif alien['color'] == 'yellow':
    alien['color'] = 'red'
    alien['speed'] = 'fast'
    alien['points'] = 15
for alien in aliens[0:5]:
 print(alien)
print("...")

#Список в словаре
# Сохранение информации о заказанной пицце.
pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }#список в словаре
# Описание заказа.
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
 print("\t" + topping)

#В цикле for словаря создается другой цикл для перебора списка языков, связанных с каждым участником:

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
 print("\n" + name.title() + "'s favorite languages are:")
 for language in languages:
   print("\t" + language.title())

#В следующем примере о каждом пользователе хранятся три вида информации: имя, фамилия и место жительства. Чтобы получить доступ к этой информации, переберите имена пользователей и словарь с информацией, связанной с каждым именем:

users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }
for username, user_info in users.items():
  print("\nUsername: " + username)
  full_name = user_info['first'] + " " + user_info['last']
  location = user_info['location']
  print("\tFull name: " + full_name.title())
  print("\tLocation: " + location.title())

#DZ
devid = {
  'first_name' : 'devid', 
  'last_name' : 'stupid', 
  'age' : 19,  
  'city' : 'zalupa'
  }
bob = {
  'first_name' : 'bob', 
  'last_name' : 'sinkler', 
  'age' : 21, 
  'city' : 'zelec'
  }
people = [devid, bob]
for peopl in people:
  full_name = peopl['first_name'] + ' ' + peopl['last_name']
  print("\nFull name: " + full_name.title() + "\nLocation: " + peopl['city'] + "\nAge: " + str(peopl['age']))


#DZ2
kit = {'name' : 'kit', 'color' : 'black', 'age' : '1.5', 'what' : 'cat'}
dig = {'name' : 'dig', 'color' : 'green', 'age' : '7', 'what' : 'dog'}
masha = {'name' : 'masha','color' : 'white', 'age' : '19', 'what' : 'woman'}
pets = [kit, dig, masha]
print(type(kit))
print(type(dig))
print(type(masha))
for pet in pets:
  print("\nFull Name: " + pet['name'].title() + "\nColor is: " + pet['color'].title() + "\nAge: " + pet['age'] + "\nWho is: " + pet['what'].title())

cities = {
  'Москва' : {'country' : 'РФ', 'population' : 'Мажоры', 'fact' : 'Не резиновая'},
  'Иркутск' : {'country' : 'РФ', 'population' : 'Мажоры', 'fact' : 'Не резиновая'}, 
  'Калиниград' : {'country' : 'РФ', 'population' : 'Кант', 'fact' : 'Почти Европа'}}
#info_msk = {'country' : 'РФ', 'population' : 'Мажоры', 'fact' : 'Не резиновая'}
#info_irk = {'country' : 'РФ', 'population' : 'Буряты', 'fact' : 'сибирь'}
#info_kgd = {'country' : 'РФ', 'population' : 'Кант', 'fact' : 'Почти Европа'}
print(cities['Москва'])
