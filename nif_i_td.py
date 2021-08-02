#Если регистр символов важен, такое поведение приносит пользу. Но если проверка должна выполняться на уровне символов без учета регистра, преобразуйте значение переменной к нижнему регистру перед выполнением сравнения:
car = 'Audi'
car.lower() == 'audi'
#true

#Проверка неравенства
#Если вы хотите проверить, что два значения различны, используйте комбинацию из восклицательного знака и знака равенства (!=). Восклицательный знак представляет отрицание, как и во многих языках программирования.

#Чтобы проверить, что два условия истинны одновременно, объедините их ключевым словом and;

#Ключевое слово or тоже позволяет проверить несколько условий, но результат общей проверки является истинным в том случае, когда истинно хотя бы одно или оба условия.

#Чтобы узнать, присутствует ли заданное значение в списке, воспользуйтесь ключевым словом in. Допустим, вы пишете программу для пиццерии. Вы создали список дополнений к пицце, заказанных клиентом, и хотите проверить, входят ли некоторые дополнения в этот список.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
True
'pepperoni' in requested_toppings
False

#В других случаях программа должна убедиться в том, что значение не входит в список. Для этого используется ключевое слово not
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(user.title() + ", you can post a response if you wish.")

#Результат логического выражения равен True или False, как и результат условного выражения после его вычисления. Логические выражения часто используются для проверки некоторых условий — например, запущена ли компьютерная игра или разрешено ли пользователю редактирование некоторой информации на сайте:
game_active = True
can_edit = False

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#DZ
two = 2+2 
lesha = 'Malchik'
irina = 'devochka'
i = 'debil'
spisok = ['debil', 'azzazin']
print("lesha == Malchik, True")
print(lesha == 'Malchik')
print("lesha == malchik, True")
print(lesha.lower() == 'malchik')
if two == 2:
  print("two == 2")
else:
  print("two == 4")
  print(two == 4)
if 'debil' in spisok:
  print("'debil' in spisok it is True")
  print('debil' in spisok)


#Блок if-else в целом похож на команду if, но секция else определяет действие или набор действий, выполняемых при неудачной проверке.
#Нередко в программе требуется проверять более двух возможных ситуаций; для таких ситуаций в Python предусмотрен синтаксис if-elif-else
#Код может содержать сколько угодно блоков elif.

alien_color = 'green'
if 'green' in alien_color:
  print('+5 OK')
else:
  print('+1 OK')

#Когда имя списка используется в условии if, Python возвращает True, если список содержит хотя бы один элемент; если список пуст, возвращается значение False. 

hello = ['admin', 'a', 'b', 'c', 'w']
if len(hello):
  if 'admin' in hello:
   print('Hello admin, would you like to see a status report?')
  if 'a' in hello:
   print('Hello a, thank you for logging in again')
  if 'b' in hello:
   print('Hello b, thank you for logging in again')
  if 'c' in hello:
   print('Hello c, thank you for logging in again')
  if 'w' in hello:
   print('Hello w, thank you for logging in again')
else:
  print('spisok pust')
#Функция len с помощью можно проверить пуст ли список. если len() выдает 0, то выводится значение False