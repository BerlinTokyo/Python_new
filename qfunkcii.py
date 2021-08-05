#Определение функции
#Вот простая функция greet_user(), которая выводит приветствие:

def greet_user():
  print("Hello!")

greet_user()
#Все строки с отступами, следующие за def greet_user():, образуют тело функции.

#При вызове greet_user() укажите имя (например, 'jesse') в круглых скобках:
def greet_user(username):
 print("Hello, " + username.title() + "!")

greet_user('jesse')
#Функция greet_user() определена так, что для работы она должна получить значение переменной username. После того как функция будет вызвана и получит необходимую информацию (имя пользователя), она выведет правильное приветствие. Переменная username в определении greet_user() — параметр, то есть условные данные, необходимые функции для выполнения ее работы. Значение 'jesse' в greet_user('jesse') — аргумент, то есть конкретная информация, переданная при вызове функции. Вызывая функцию, вы заключаете значение, с которым функция должна работать, в круглые скобки. В данном случае аргумент 'jesse' был передан функции greet_user(), а его значение было сохранено в переменной username.

#Определение функции может иметь несколько параметров, и может оказаться, что при вызове функции должны передаваться несколько аргументов. Существуют несколько способов передачи аргументов функциям. Позиционные аргументы перечисляются в порядке, точно соответствующем порядку записи параметров; именованные аргументы состоят из имени переменной и значения; наконец, существуют списки и словари значений. Рассмотрим все эти способы.
#При вызове функции каждому аргументу должен быть поставлен в соответствие параметр в определении функции. Проще всего сделать это на основании порядка перечисления аргументов. Значения, связываемые с аргументами подобным образом, называются позиционными аргументами.
def describe_pet(animal_type, pet_name):
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
#видно, что функции должен передаваться тип животного (animal_type) и его имя (pet_name). При вызове describe_pet() необходимо передать тип и имя — именно в таком порядке. В этом примере аргумент 'hamster' сохраняется в параметре animal_type, а аргумент 'harry' сохраняется в параметре pet_name

#Функция может вызываться в программе столько раз, сколько потребуется.
describe_pet('dog', 'willie')

#Именованный аргумент представляет собой пару «имя—значение», передаваемую функции. 
#Перепишем программу pets.py с использованием именованных аргументов при вызове describe_pet():
def describe_pet(animal_type, pet_name):
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')

def describe_pet(pet_name, animal_type='dog'): #Значения по умолчанию
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
#Обратите внимание: в определении функции пришлось изменить порядок параметров. 
describe_pet(pet_name='harry', animal_type='hamster')
#Так как аргумент для параметра animal_type задан явно, Python игнорирует значение параметра по умолчанию.

#DZ
w = 'You are Ri is: '
c = 'You are Text is: '
a = input(w)
b = input(c)
def make_shirt(Ri,text):
  print("You RI: " + Ri + "\nYou Text: " + text)
make_shirt(Ri=a,text=b)

#Функция не обязана выводить результаты своей работы. Вместо этого она может обработать данные, а затем вернуть значение или набор сообщений. Значение, возвращаемое функцией, называется возвращаемым значением. Команда return передает значение из функции в строку, в которой эта функция была вызвана. Возвращаемые значения помогают переместить бульшую часть рутинной работы в вашей программе в функции, чтобы упростить основной код программы.
#Рассмотрим функцию, которая получает имя и фамилию и возвращает аккуратно отформатированное полное имя:
def get_formatted_name(first_name, last_name):
  full_name = first_name + ' ' + last_name
  return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#Аргументу можно придать пустое значение, чтобы н игнорировался если это нужно пользователю.
#Чтобы функция get_formatted_name() работала без второго имени, следует назначить для параметра middle_name пустую строку значением по умолчанию и переместить его в конец списка параметров:
def get_formatted_name(first_name, last_name, middle_name=''):
  if middle_name:
    full_name = first_name + ' ' + middle_name + ' ' + last_name
  else:
    full_name = first_name + ' ' + last_name
  return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Функция может вернуть любое значение, нужное вам, в том числе и более сложную структуру данных (например, список или словарь). Так, следующая функция получает части имени и возвращает словарь, представляющий человека:
def build_person(first_name, last_name):
  person = {'first': first_name, 'last': last_name}
  return person
musician = build_person('jimi', 'hendrix')
print(musician)

#Функцию можно легко расширить так, чтобы она принимала дополнительные значения: — второе имя, возраст, профессию или любую другую информацию о человеке, которую вы хотите сохранить. Например, следующее изменение позволяет также сохранить возраст человека:
def build_person(first_name, last_name, age=''):
 person = {'first': first_name, 'last': last_name}
 if age:
   person['age'] = age
 return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#Функции могут использоваться со всеми структурами Python, уже известным вам. 
def get_formatted_name(first_name, last_name):
 """Возвращает аккуратно отформатированное полное имя."""
 full_name = first_name + ' ' + last_name
 return full_name.title()
while True:
 print("\nPlease tell me your name:")
 print("(enter 'q' at any time to quit)")

 f_name = input("First name: ")
 if f_name == 'q':
   break

 l_name = input("Last name: ")
 if l_name == 'q':
   break

 formatted_name = get_formatted_name(f_name, l_name)
 print("\nHello, " + formatted_name + "!")

#Передача списка
#В следующем примере список имен передается функции greet_users(), которая выводит приветствие для каждого пользователя по отдельности:
def greet_users(names):
 """Вывод простого приветствия для каждого пользователя в списке."""
 for name in names:
    msg = "Hello, " + name.title() + "!"
    print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

def print_models(unprinted_designs, completed_models):
 """
 Имитирует печать моделей, пока список не станет пустым.
 Каждая модель после печати перемещается в completed_models.
 """
 while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Имитация печати модели на 3D-принтере.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

def show_completed_models(completed_models):
 """Выводит информацию обо всех напечатанных моделях."""
 print("\nThe following models have been printed:")
 for completed_model in completed_models:
    print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Чтобы передать функции копию списка, можно поступить так:  
#      имя_функции(имя_списка[:]) 
#Синтаксис среза [:] создает копию списка для передачи функции. Если удаление элементов из списка unprinted_designs в print_models.py нежелательно, функцию print_models() можно вызвать так:
#      print_models(unprinted_designs[:], completed_models)
makes = ['tini', 'yri', 'tobian']
def show_magicians(makes):
  for make in makes:
    print(make)
show_magicians(makes)  

def make_great(makes):
  make_great = "Great " + str(makes) 
  makes = make_great
  return(makes)
make_great(makes)
show_magicians(makes) 