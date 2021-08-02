names = ['Olejshka', 'Elena', 'Irishka', 'Fuckinfuck']
print(names[0], names[1], names[2], names[3])
print("Yor'e my friend", names[0])
print("Yor'e my friend", names[1])
print("Yor'e my friend", names[2])
print("Yor'e my friend", names[3])
names[3] = 'NoFuckinfuck'
print(names[3])
print(names)
names.append('List')
print(names)

#Метод insert() позволяет добавить новый элемент в произвольную позицию списка. Для этого следует указать индекс и значение нового элемента.
names.insert(0, 'list')
print(names)

#Удаление эллементов списка с помощью del
del names[0] 
del names[4]
print(names)

#Метод pop() удаляет последний элемент из списка, но позволяет работать с ним после удаления.

popped_names = names.pop()
print(names)
print(popped_names)

#Вызов pop() может использоваться для удаления элемента в произвольной позиции списка; для этого следует указать индекс удаляемого элемента в круглых скобках.
popped_names = names.pop(2)
print("Eeee boy, it is:" + " " + popped_names)

#Иногда позиция удаляемого элемента неизвестна. Если вы знаете только значение элемента, используйте метод remove().
#Допустим, из списка нужно удалить значение 'ducati':

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#Метод remove() также может использоваться для работы со значением, которое удаляется из списка. Следующая программа удаляет значение 'ducati' и выводит причину удаления:

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
#Метод remove() удаляет только первое вхождение заданного значения. Если существует вероятность того, что значение встречается в списке более одного раза, используйте цикл для определения того, были ли удалены все вхождения данного значения. О том, как это делать, рассказано в главе 7.

#Создадим список гостей
Gosti = ['lesha', 'irina', 'lena', 'tima']
print(Gosti)
print(Gosti[0].title()+ " " +  "Hello friend, go ko mne)")
print(Gosti[1].title()+ " " +  "Hello friend, go ko mne)")
print(Gosti[2].title()+ " " +  "Hello friend, go ko mne)")
print(Gosti[3].title()+ " " +  "Hello friend, go ko mne)")
#Tima ne pridet(
ne_pridet = 'tima'
Gosti.remove(ne_pridet)
Gosti.append('Karpyk')
print(Gosti)
print(Gosti[0].title()+ " " +  "Hello friend, go ko mne)")
print(Gosti[1].title()+ " " +  "Hello friend, go ko mne)")
print(Gosti[2].title()+ " " +  "Hello friend, go ko mne)")
print(Gosti[3].title()+ " " +  "Hello friend, go ko mne)")
#Добавим гостей
Gosti = ['lesha', 'irina', 'lena', 'tima']
Gosti.insert(0, 'Karpyk')
Gosti.append('Vitia')
print(Gosti)
#Оставим всего три гостя
print('Idite nahyi vsego dva gostia')
Karp = Gosti.pop(0)
print(Karp + " " + "idi nahyi")
Vit = Gosti.pop(4)
print(Vit + " idi nahyi" )
tim = Gosti.pop(3)
print(tim + " idi nahyi")
print(Gosti)
#ОЧистим список
del Gosti[0]
del Gosti[0]
del Gosti[0]
print(Gosti)

#Метод sort() позволяет относительно легко отсортировать список. Предположим, имеется список машин, и вы хотите переупорядочить эти элементы по алфавиту. Чтобы упростить задачу, предположим, что все значения в списке состоят из символов нижнего регистра.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Список также можно отсортировать в обратном алфавитном порядке
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#Чтобы сохранить исходный порядок элементов списка, но временно представить их в отсортированном порядке, можно воспользоваться функцией sorted(). Функция sorted() позволяет представить список в определенном порядке, но не изменяет фактического порядка элементов в списке.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
#Функции sorted() также можно передать аргумент reverse=True

#Определение длины списка. Вы можете быстро определить длину списка с помощью функции len(). Список в нашем примере состоит из четырех элементов, поэтому его длина равна 4:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
#4

country = ['usa', 'russian federation','ukraine', 'kuba', 'iadayn']
print(country)
print(sorted(country))
print(country)
print(sorted(country, reverse=True))
country.reverse()
print(country)
country.reverse()
print(country)
country.sort()
print(country)
country.sort(reverse=True)
print(country)
Gosti = ['lesha', 'irina', 'lena', 'tima']
print('Гостей позвал:', len(Gosti))
