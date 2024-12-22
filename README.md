# 3. Переменные и объекты

![img.png](img/img.png)

---

## Вступление

Добро пожаловать в тему переменных и объектов!

В этой теме научитесь создавать и использовать переменные, узнаете о том, как работают объекты и
как присваивать значения переменным. Изучим, как выбирать правильные имена для переменных и почему это важно.
Также научитесь получать пользовательский ввод с клавиатуры и использовать полученные данные в своих программах.

---

## Содержание

- [Объекты](#объекты)
- [Функция `id()`](#функция-id)
- [Атомарные и ссылочные типы данных](#атомарные-и-ссылочные-типы-данных)
- [Функция `type()`](#функция-type)
- [Переменные](#переменные)
- [Имена идентификаторов](#имена-идентификаторов)
- [Функция input()](#функция-input)
- [Задания](#задания)

---

## Объекты

В Python всё, что мы используем в коде - от простых типов данных: булевы значения, числа, строки
до более сложных структур: списки, множества, функции и даже программы - представляет собой объекты.

Объект в Python можно представить как прозрачный пластиковый ящик, который хранит информацию.
У каждого объекта есть свой тип и набор свойств, который определяет его поведение, какие операции
можно выполнить с этим объектом. Это похоже на то, как в реальной жизни различные предметы
используются для выполнения определённых задач.

Например, объект строкого типа `str` можно конкатенировать[^1] (объединять) с другими строками,
но нельзя объединить строку с объектами другого типа.

Тип объекта также определяет, можно ли изменить его содержимое.
Некоторые объекты называются **неизменяемыми**, а другие - **изменяемыми**.

**Пример из жизни**:

- Представьте себе ящик с яблоками. Этот ящик можно рассматривать как объект типа `список`,
  поскольку он может содержать несколько элементов других типов. Если вы хотите узнать,
  сколько яблок в ящике, вы можете обратиться к свойству списков `длина`. Если вы хотите
  добавить в ящик ещё одно яблоко, это будет возможно, потому что список - изменяемый объект.
- Однако, если ящик с яблоками - это объект типа `кортеж`, то он будет **неизменяемым**.
  В таком случае вы не сможете добавить новое яблоко или удалить существующее.
  Кортеж можно только _просматривать_, но любые изменения невозможны.

Каждый объект в Python имеет уникальный идентификатор, который можно получить с помощью встроенной
функции `id()`, которая позволяет различать объекты, даже если они содержат одинаковые данные.

---

## Функция `id()`

Встроенная функция `id()` возвращает уникальный идентификатор объекта в его жизненном цикле[^2].
Этот идентификатор не является физическим адресом в памяти[^3], а служит для различения объектов.
Он полезен, например, для отслеживания того, какие переменные ссылаются на один и тот же объект.

**Пример**:

```python
# Создаем несколько объектов различных типов
num = 5
message = "Hello"
flag = True

# Выводим их идентификаторы
print("Идентификатор num:", id(num))
print("Идентификатор message:", id(message))
print("Идентификатор flag:", id(flag))

# Создаем новые переменные, которые ссылаются на те же объекты
temp_num = num
temp_message = message

# Выводим их идентификаторы
print("\nИдентификатор temp_num:", id(temp_num))
print("Идентификатор temp_message:", id(temp_message))
```

Этот код выведет следующее:

```
Идентификатор num: 10865416
Идентификатор message: 140346935686960
Идентификатор flag: 9810080

Идентификатор temp_num: 10865416
Идентификатор temp_message: 140346935686960
```

Переменная `temp_num` ссылается на тот же объект, что и переменная `num`, поэтому они имеют одинаковый идентификатор.
Аналогично, переменная `temp_message` ссылается на тот же объект, что и переменная `message`.

---

## Атомарные и ссылочные типы данных

В Python типы данных делятся на 2 вида: атомарные и ссылочные.

Атомарные типы данных:

- числа - `int`, `float`;
- строки - `str`;
- булевы - `bool`;
- отсутствие значения - `None`.

Ссылочные типы данных:

- списки - `list`;
- кортежи - `tuple`;
- множества - `set`;
- словари - `dict`;
- функции - `function`;
- классы - `class`.

Отличия между ними в том, что атомарные типы данных при присваивании переменной, **передаются по значению**,
а ссылочные типы данных при присваивании переменной **передаются по ссылке**.

- По значению.

    - Это означает, что если два объекта атомарного типа имеют одинаковые значения,
      они будут занимать одно и то же место в памяти. Python может использовать **интернирование**[^4]
      строк или других числовых объектов для экономии памяти.

- По ссылке:

    - То есть переменные будут ссылаться на один и тот же объект в памяти,
      что приводит к тому, что изменения в одном объекте могут повлиять на другой.

- **Пример из жизни**:

    - Представьте, что у вас есть два друга, которые используют одну и ту же книгу.
      Если один из них перепишет страницу, другой друг увидит эти изменения.
    - В случае с атомарными типами это больше похоже на ситуацию, когда каждый друг получает свою собственную
      копию книги, и если один из друзей переписывает страницы, это не повлияет на другую книгу.

**Пример**:

```python
first_num = 10
second_num = 10
message_1 = "hello"
message_2 = "hello"
numbers_one = [1, 2, 3]
numbers_two = [1, 2, 3]

print("Идентификатор first_num:", id(first_num))
print("Идентификатор second_num:", id(second_num))
print("Идентификатор message_1:", id(message_1))
print("Идентификатор message_2:", id(message_2))
print("Идентификатор numbers_one:", id(numbers_one))
print("Идентификатор numbers_two:", id(numbers_two))
```

Этот код выведет следующее:

```
Идентификатор first_num: 10865576
Идентификатор second_num: 10865576
Идентификатор message_1: 140665366967152
Идентификатор message_2: 140665366967152
Идентификатор numbers_one: 140665369344704
Идентификатор numbers_two: 140665366956224
```

Переменные `first_num` и `second_num` ссылаются на один и тот же объект, так как значение числа `10`
является неизменяемым. Также переменные `message_1` и `message_2` ссылаются на один и тот же объект строки `"hello"`
является неизменяемым. Однако переменные `numbers_one` и `numbers_two` ссылаются на разные объекты,
так как списки являются изменяемыми и каждая переменная создает новый объект списка.

---

## Функция `type()`

Встроенная функция `type()` позволяет узнать тип объекта.
Тип объекта определяет, какие действия можно с ним выполнять и как он ведет себя в различных ситуациях.

**Пример**:

```python
number = 42
print(type(number))  # <class 'int'>
```

Этот код покажет тип переменной `number`, который в данном случае является целым числом `int`.
Аналогичным образом можно узнать тип любых объектов:

**Пример**:

```python
some_text = "Hello, world!"
print(type(some_text))  # <class 'str'>
```

Знание типа объекта может быть полезно в различных ситуациях. Например, если вы хотите выполнить
определенную операцию в зависимости от типа объекта.

**Пример**:

```python
number = 42

if type(number) == int:
    print("Переменная является целым числом.")
    print("Удваиваем его значение:", number * 2)
```

Этот код выполнит блок внутри условия только в случае, если тип переменной `number` - целое число.

Одной из интересных особенностей Python является то, что булевы значения, (тип `bool`) является подклассом типа `int`.
Это значит, что значения `False` и `True` в Python на самом деле являются целым числом `0` и `1` соответственно.

**Пример**:

```python
first = True
second = False

print(type(first))  # <class 'bool'>
print(type(second))  # <class 'bool'>

print(type(first) == bool)  # True
print(type(second) == bool)  # True

print(type(first) == int)  # False
print(type(second) == int)  # False
```

В некоторых случаях функция `type()` может быть полезной, но в большинстве ситуаций рекомендуется использовать
`isinstance()`, так как она не только проверяет точный тип объекта, но и учитывает возможность наследования.

> О функции `isinstance()` более подробно поговорим в теме ООП.

**Пример**:

```python
first = True
second = False

print(type(first))  # <class 'bool'>
print(type(second))  # <class 'bool'>

print(isinstance(first, bool))  # True
print(isinstance(second, bool))  # True

print(isinstance(first, int))  # True, потому что учитывает возможность наследования
print(isinstance(second, int))  # True
```

Использование этих функций в правильном контексте очень важно. Мы надеемся, что к концу обучения
вы будете точно знать, когда следует использовать `type()`, а когда - `isinstance()`.

---

## Переменные

Переменные в программировании - это _контейнеры_ для хранения данных, но в Python переменные не привязаны
к конкретным типам данных. Это значит, вы можете присваивать переменной значение любого типа: число,
строку, список и т.д. Для того чтобы присвоить значение переменной, используется оператор присваивания `=`.

**Пример**:

```python
x = 25
print(x)  # 25
```

Здесь мы присваиваем переменной `x` значение `25`. Когда мы используем имя переменной `x` в коде,
Python будет работать с этим значением.

> **Важное замечание**: В Python переменные не хранят данные прямо. Они являются ссылками на объекты в памяти.
> Когда мы присваиваем переменной значение, мы фактически создаем ссылку на объект, который содержит это значение.

**Пример**:

```python
x = 8
print(type(x))  # <class 'int'>

x = "Hello, World!"
print(type(x))  # <class 'str'>
```

Сначала переменная `x` хранит целое число `8`. Используя функцию `type()`, мы проверяем тип значения и видим,
что это `int`. Затем мы меняем значение переменной `x` на строку `"Hello, World!"`, и снова используем `type()`,
теперь тип - `str`.

> Важно понимать, что переменные в Python могут быть переназначены в любой момент и
> они будут указывать на новый объект в памяти.

**Пример из жизни**:

- Вы сдаёте куртку в гардероб и получаете номерок, например, `x`. Этот номерок указывает на вашу куртку.
- Если вы сдадите другую куртку под тот же номерок `x`, гардеробщик просто заменит старую куртку на новой.
  Номерок `x` остался тем же, но куртка изменилась. Старая куртка отправляется на _утилизацию_, ведь больше никто
  не может её получить (так как номерок теперь указывает на новую куртку). _Да, такое в реальной жизни с нашими
  куртками не происходит, но представьте это для понимания примера._
- При этом, если вы передадите свой номерок другому человеку, он сможет получить доступ к той же куртке.

> - Куртка - это объект в памяти
> - Номерок - это переменная

### Почему важно использовать переменные?

Переменные делают ваш код более понятным и удобным для чтения. Если вы дадите переменным осмысленные имена,
ваш код станет легче воспринимаемым, а также будет проще в изменении.

**Пример**:

```python
questions_count = 10
```

Здесь мы используем переменную с осмысленным именем `questions_count`, чтобы указать количество вопросов.
Это делает код более читаемым, по сравнению с использованием _магических чисел_, как в следующем примере.

### Проблема "магических чисел"

Часто бывает так, что в коде встречаются числа, значение которых не очевидно и может вызвать путаницу.
Такие числа называются - **магическими числами**

**Пример**:

```python
num = 20
print("Общее количество кошек:", num // 4)
```

Здесь мы делим `num` на `4`, но непонятно, что эти числа означают.

- Почему переменная `num` равна `20`?
- Почему мы делим на `4`?

Лучше использовать переменные с осмысленными именами и выносить магические значения в отдельные переменные.

**Пример**:

```python
num_of_paws = 20
cat_paws = 4

print("Общее количество кошек:", num_of_paws // cat_paws)
```

Теперь мы знаем, что `20` - это общее количество лап, а переменная `cat_paws` хранит количество лап
у одной кошки. Это улучшает читаемость кода и делает его более понятным.

### Множественное присвоение

Множественное присвоение позволяет в одной строке присвоить значения нескольким переменным
с помощью одного оператора присваивания:

```python
x, y, z = 10, "Programming", 30
```

В этом примере мы присваиваем значения `10`, `"Programming"`, `30` переменным `x`, `y` и `z` соответственно.

> Важно: количество переменных и количество значений должно быть одинаковым.

### Каскадное присваивание

```python
a = b = c = 50
```

Здесь мы присваиваем значение `50` сразу трем переменным: `a`, `b`, и `c`. Присваивание происходит каскадом:
это значит, сначала переменной `c` присваивается значение `50`, затем это же значение присваивается
переменным `b` и `a`.

Использование переменных делает ваш код более чистым и понятным, как для других разработчиков, так и для вас в будущем.
Когда вы возвращаетесь к своему коду спустя время, переменные с осмысленными именами помогут быстро понять,
что происходит в вашем коде.

---

## Имена идентификаторов

Имена идентификаторов - это названия, которые используются в коде. Пока вы знакомы только с переменными, но в будущем
вам предстоит работать с функциями, классами, пакетами и др. Все они подчиняются одинаковым правилам.

**Общие правила для именования идентификаторов:**

- Имя может содержать буквы, цифры и символы подчеркивания.
- Имя должно начинаться с буквы или символа подчеркивания `_`.
- Имя должно быть уникальным в пределах своей области видимости.
- Имя не должно быть [зарезервированным словом](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
  или названием [встроенной функции](https://docs.python.org/3/library/functions.html#built-in-functions) в Python.

> - Область видимости будет подробно рассмотрена в разделе о функциях.

**Примеры правильных имен идентификаторов:**

```
name
age
total_price
_my_variable
ElectricCar
calculate_sum
```

**Примеры неправильных имен идентификаторов:**

```
123number  # начинается с цифры
my-variable  # содержит дефис
total price  # содержит пробел
if  # зарезервированное слово в Python
```

В повседневной жизни мы разделяем слова пробелами, но в коде это недопустимо. Вместо пробела используйте
символ подчеркивания для разделения слов.

В других языках программирования могут использоваться разные способы разделения слов.

- `num_of_cats` - **змеиный регистр**, то что используется в Python.
- `numOfCats` - **верблюжий регистр**, обычно используется в языках, подобных C.
- `NumOfCats` - **регистр Паскаля**, отличие от верблюжьего регистра в том, что каждое
  слово начинается с заглавной буквы.
- `num-of-cats` - **кебаб-регистр**, обычно используется в HTML и CSS.

В Python мы придерживаемся змеиного регистра, но при изучении объектно-ориентированного программирования
также будем использовать регистр Паскаля для имен классов.

Кроме того, Python имеет список зарезервированных слов, которые нельзя использовать в качестве имен идентификаторов.
К ним относятся слова `if`, `else`, `for`, `while`и др. Полный список
[зарезервированных слов](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
и [встроенных функций](https://docs.python.org/3/library/functions.html#built-in-functions) можно найти в
документации Python 3. Если вы попытаетесь использовать зарезервированное слово в качестве имени идентификатора,
возникнет ошибка `SyntaxError`.

Правильный выбор имен для идентификаторов крайне важен. Плохо выбранные имена могут затруднить понимание
вашего кода как другим разработчикам, так и вам в будущем.

---

## Функция `input()`

Получение данных от пользователя неотъемлемая часть работы большинства программ. В зависимости от задачи,
данные могут поступать в программу разными способами, например из файлов, через сеть, из баз данных и т.д.
Мы рассмотрим способ ввода данных _с клавиатуры_. Для этого в Python используется встроенная функция `input()`,
которая позволяет считывать информацию, введенную пользователем в консоли.

> Функция `input()` позволяет пользователю вводить данные в консоли и возвращает введенное значение.

Очень важно понимать, что функция `input()` полученную информацию _возвращает_ как тип `str`, которую
можно сохранить в переменной и использовать дальше в программе.

**Пример**:

```python
name = input("Введите ваше имя: ")

print("Привет, " + name + "!")
```

В примере выше программа выводит на экран сообщение с просьбой `Введите ваше имя: ` и ожидает, пока пользователь
не вводит свое имя и не нажимает `Enter`, после этого полученное значение сохраняется в переменной `name`,
и программа выводит на экран приветственное сообщение.

> Обратите внимание на аргумент, переданный в функцию `input()`, этот аргумент представляет
> собой строку, которая будет выведена в консоль для запроса ввода. Она может быть любой строкой, которая
> поможет пользователю понять, что именно ему нужно ввести. В нашем случае это `"Введите ваше имя: "`.

Что если нужно получить числовые данные, в таком случае нужно явно преобразовать полученное значение в число,
используя функции `int()` или `float()`.

**Пример**:

```python
age = input("Введите ваш возраст: ")
age = int(age)

print("Через 10 лет вам будет", age + 10, "лет")
```

В этом примере программа запрашивает возраст пользователя, сохраняет его в переменную `age`, после этого преобразует
введенную строку в целое число с помощью функции `int()`, а затем выводит информацию о возрасте через 10 лет.

Мы можем сразу преобразовать введенное значение в нужный нам тип данных, чтобы сделать код более лаконичным:

**Пример**:

```python
age = int(input("Введите ваш возраст: "))

print("Через 10 лет вам будет", age + 10, "лет")
```

Если пользователь введет символы, которые нельзя преобразовать в число, то программа выдаст ошибку `ValueError`:

---

## Заключение

Поздравляем! Вы успешно освоили основы работы с переменными и теперь понимаете, как они связаны с объектами.
Вы узнали, как правильно выбирать имена для переменных, чтобы код был читаемым и понятным, а также познакомились
с функцией получения пользовательского ввода.

Эти знания являются важной основой для дальнейшего изучения Python и создания более сложных программ.
В следующей теме мы перейдем к основным операторам Python.

---

## [Задания](./tasks/TASKS.md)

---

## Полезные ссылки

- [Skillbox: Нотации в программировании](https://skillbox.ru/media/code/notatsii-v-programmirovanii/)
- [Pythonchik: Именование в Python - как выбирать имена и почему это важно](https://pythonchik.ru/osnovy/imenovanie-v-python)

[^1]: Конкатенация строк - это процесс последовательного объединения двух или более строк в единое целое.
[^2]: Жизненный цикл объекта - это период времени между созданием объекта[^5] и его уничтожением[^6].
[^3]: Физический адрес в памяти - это номер ячейки в оперативной памяти компьютера. Зная этот номер, процессор
непосредственно обращается в нужное место оперативной памяти за необходимыми данными. Реальное место расположения
объекта в оперативной памяти, недоступно для пользователей в высокоуровневых языках программирования.
[^4]: Интернирование строк - это метод для оптимизации использования памяти и повышения производительности
за счёт повторного использования неизменяемых объектов вместо создания новых экземпляров.
Суть интернирования в том, что Python сохраняет в памяти только одну копию каждого отдельного строкового
значения независимо от того, сколько раз на него ссылаются. Это снижает потребление памяти и ускоряет
сравнение строк, поскольку их можно сравнивать по адресу памяти вместо сравнения каждого символа.
[^5]: **Создание объекта** - это выделение памяти для хранения объекта.
[^6]: **Удаление объекта** - это освобождение памяти, используемой для хранения объекта.
