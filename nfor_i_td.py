magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician)

pizec = ['a', 'b', 'c']
for piza in pizec:
  print('I like:' + piza)

#Функция range() упрощает построение числовых последовательностей. Например, с ее помощью можно легко вывести серию чисел:
for value in range(1,5):
 print(value)
#И хотя на первый взгляд может показаться, что он должен вывести числа от 1 до 5,
#на самом деле число 5 не выводится
#В этом примере range() выводит только числа от 1 до 4. Перед вами еще одно проявление «смещения на 1», часто встречающегося в языках программирования. При выполнении функции range() Python начинает отсчет от первого переданного значения и прекращает его при достижении второго. Так как на втором значении про

#Если вы хотите создать числовой список, преобразуйте результаты range() в список при помощи функции list(). Если заключить вызов range() в list(), то результат будет представлять собой список с числовыми элементами.
#В примере из предыдущего раздела числовая последовательность просто выводилась на экран. Тот же набор чисел можно преобразовать в список вызовом list():
numbers = list(range(1,6))
print(numbers)

#Функция range() также может генерировать числовые последовательности, пропуская числа в заданном диапазоне. Например, построение списка четных чисел от 1 до 10 происходит так:
even_numbers = list(range(2,11,2))
print(even_numbers)
#В этом примере функция range() начинает со значения 2, а затем увеличивает его на 2. Приращение 2 последовательно применяется до тех пор, пока не будет достигнуто или пройдено конечное значение 11

#С помощью функции range() можно создать практически любой диапазон чисел. Например, как бы вы создали список квадратов всех целых чисел от 1 до 10? В языке Python операция возведения в степень обозначается двумя звездочками (**).
squares = []
for value in range(1,11):
  square = value**2
  squares.append(square)
  print(squares)
#Чтобы сделать код более компактным, можно опустить временную переменную square и присоединять каждое новое значение прямо к списку:
squares = []
for value in range(1,11):
  squares.append(value**2)

#Некоторые функции Python предназначены для работы с числовыми списками.
#Например, вы можете легко узнать минимум, максимум и сумму числового списка:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

#В следующем примере список квадратов, знакомый вам по предыдущим примерам, строится с использованием генератора списка:
squares = [value**2 for value in range(1,11)]
print(squares)

for do20 in list(range(1, 21)):
  print(do20)

do10000 = list(range(1, 10001))
print(do10000)
print(min(do10000))
print(max(do10000))
print(sum(do10000))
for nechet in range(1, 21, 2):
  print(nechet)
for troika in range(3, 33, 3):
  print(troika)

for kube in range(1, 11,):
  kubes = kube**3
  print(kubes)

cubes = [sz**3 for sz in range(1,11)]
print(cubes)

#Также можно работать с конкретным подмножеством элементов списка; в Python такие подмножества называются срезами (slices).

#Скажем, чтобы вывести первые три элемента списка, запросите индексы с 0 по 3, и вы получите элементы 0, 1 и 2. В следующем примере используется список игроков команды:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
#Если первый индекс среза не указан, то Python автоматически начинает срез от начала списка:
print(players[:4])
#Аналогичный синтаксис работает и для срезов, включающих конец списка. Например, если вам нужны все элементы с третьего до последнего, начните с индекса 2 и не указывайте второй индекс:
print(players[2:])
#Например, чтобы отобрать последних трех игроков, используйте срез players[-3:]:
print(players[-3:])

#Копирование списка
#Чтобы скопировать список, создайте срез, включающий весь исходный список без указания первого и второго индекса ([:]). Эта конструкция создает срез, который начинается с первого элемента и завершается последним; в результате создается копия всего списка.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print('The first three items in the list are:')
print(my_foods[:3])
nambers = ['one', 'two', 'three', 'four', 'five', 'six']
print('Three items from the middle of the list are:')
print(nambers[2:5])
print('The last three items in the list are:')
print(nambers[-3:])

#Моя пицца, твоя пицца: начните с программы из упражнения 4-1. Создайте копию
#списка с видами пиццы, присвойте ему имя friend_pizzas. Затем сделайте следующее.
#Добавьте новую пиццу в исходный список.
#Добавьте другую пиццу в список friend_pizzas.
#Докажите, что в программе существуют два разных списка. Выведите сообщение «My
#favorite pizzas are:», а затем первый список в цикле for. Выведите сообщение «My
#friend’s favorite pizzas are:», а затем второй список в цикле for. Убедитесь в том, что
#каждая новая пицца находится в соответствующем списке.
my_pizza = ['a', 'b', 'c']
friends_pizza = my_pizza[:]
my_pizza.append('zo')
friends_pizza.append('bo')
print(my_pizza)
print(friends_pizza)
for p1 in my_pizza:
  print(p1)


#В языке Python значения, которые не могут изменяться, называются неизменяемыми (immutable), а неизменяемый список называется кортежем.
#Кортеж выглядит как список, не считая того, что вместо квадратных скобок используются круглые скобки. После определения кортежа вы можете обращаться к его отдельным элементам по индексам точно так же, как это делается при работе со списком.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#Для перебора всех значений в кортеже используется цикл for, как и при работе со списками:
for dimension in dimensions:
 print(dimension)

#Элементы кортежа не могут изменяться, но вы можете присвоить новое значение переменной, в которой хранится кортеж. Таким образом, для изменения размеров прямоугольника следует переопределить весь кортеж:
imensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
 print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)

swed = ('a', 'v', 'd', 'w')
for sweds in swed:
  print(sweds)
print('New swed')
swed = ('a', 'o', 'd', 'w')
for sweds in swed:
  print(sweds)
