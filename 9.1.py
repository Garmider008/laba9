'''Реалізувати програму, в якій кожен з алгоритмів сортування оформити як окрему
функцію. Проілюструвати механізм використання параметрів різних типів. Забезпечити
підрахунок числа необхідних порівнянь, числа обмінів і часу роботи кожної функції,
сформувавши функції оцінки ефективності методів сортування. Підготувати єдині для
всіх алгоритмів тестові вихідні дані:
• згенерована послідовність псевдовипадкових чисел, достатня для оцінки
швидкості роботи алгоритму сортування (близько 100000 цілих чисел);
• вихідна послідовність псевдовипадкових чисел, відсортована будь-яким методом
в порядку зростання;
• вихідна послідовність псевдовипадкових чисел, відсортована будь-яким методом
в порядку за спаданням;
• забезпечити програмну можливість вибору введення вихідних даних з клавіатури
до 30 вихідних чисел.
Для програми привести лістинг з результати роботи:
• вихідний масив (вивести на екран для випадку введення вихідних даних з
клавіатури);
• відсортований масив (для випадку введення вихідних даних з клавіатури один
екземпляр відсортованого масиву вивести на екран);
• показники функції оцінки ефективності методів сортування (вивести на екран).
Виконати сортування масиву цілих чисел
в порядку зростання / за спаданням елементів.
Найпростіші алгоритми сортування:
• сортування бульбашкою (bubble sort);
• сортування вибором (selection sort);
• сортування вставками (insertion sort).
Гармідер Анастасія Віталіївна 122В
'''
#імпортуємо рандом
import random
from timeit import default_timer as timer  # модуль для запису часу


a = input('Введіть + якщо хочете ввести значення з клавіатури або - якщо автоматично')
i = list()

# Функція без аргументів так як їх немає, і працює при виклику
def d():
    for a in range(1000):
        # В пустий список добавлюємо все
        # інтерплетуємо рандомні числа
        i.append(random.randint(0, 100))


if a == '-':  # За вибором робить рандомний список
    # Відтворення функції
    d()
elif a == '+':  # або з клавіатури
    for p in range(30):
        i.append(input('дещо'))
else:
    print('RETARD')
    del (i)
# не сортований список
print(i)

qw = input('Введіть + якщо хочете щоб було від меншого до більшого, і - в зворотному напрямку')
q = input('Введіть 1 - bubble, 2 - selection  3  - insertion')


def j(k):  # bubble sort
    m = 0
    n = True
    while n:
        n = False  # прапор який якщо не став True зупиняє роботу програми так як все відсортовано
        for l in range(len(
                k) - m - 1):  # від 0 до розміру -1 за умовою range і ще -1 так як ми перевіряємо ітеріруемий з наступним, а не з минулим
            if k[l] > k[l + 1]:  # перевіряємо ітеруючий з наступним
                k[l], k[l + 1] = k[l + 1], k[l]  # якщо він більший то міняємо місцями
                n = True  # і якщо з усіх виявилося що були зміни значить ще не все відсортувала програма
        m += 1  # значення яке віднімається від кожного наступного проходження


# selection sort
def r(s):
    for t in range(
            len(s) - 1):  # від 0 до розміру -1 за умовою range і ще -1 так як останній елемент буде вже відсортований
        u = t  # мінімальне значення яке дорівнює номеру ітерації
        for v in range(t + 1, len(s)):  # елементи з якими ми буде порівнювати вибраний елемент
            if s[v] < s[u]:  # якщо обраний менше ніж ітеріруємий то це в зворотному напрямку
                u = v  # вибраний елемент стає рівним ітеріруємому
        s[t], s[u] = s[u], s[t]  # та міняє їх місцями


# insertion sort
def w(arrayToSort):  # застосовуємо функцію
    a = arrayToSort  # швидка заміна
    for i in range(len(a)):  # діапазон
        v = a[i]  # заміна за індексом
        j = i  # прирівнюєм значення
        while (a[j - 1] > v) and (j > 0):  # поки значення з індексом j-1 більше числа за індексом по ітерації і воно більше 0
            a[j] = a[j - 1]  # зменшуємо і направляємось наліво
            j = j - 1  # зменшуєм
        a[j] = v  # прирівнюємо знову коли виходимо з циклу
    return a  # повертаємо відсортований список


# bubble sort в зворотньому напрямку
def we(k):
    m = 0
    n = True
    while n:
        n = False  # прапор який якщо не став True зупиняє роботу програми так як все відсортовано
        for l in range(len(
                k) - m - 1):  # від 0 до розміру -1 за умовою range і ще -1 так як ми перевіряємо ітеріруемий з наступним, а не з минулим
            if k[l] < k[l + 1]:  # перевіряємо ітеріруємий з наступним
                k[l], k[l + 1] = k[l + 1], k[l]  # якщо більший то міняємо місцями
                n = True  # і якщо з усіх виявилося що були зміни значить ще не все відсортувала програма
        m += 1  #  значення яке віднімається від кожного наступного проходження


# selection sort в зворотньому напрямку
def er(s):
    for t in range(
            len(s) - 1):  # від 0 до розміру -1 за умовою range і ще -1 так як останній елемент буде вже відсортований
        u = t  # мінімальне значення яке дорівнює номеру ітерації
        for v in range(t - 1, len(s)):  # елементи з якими ми буде порівнювати вибраний елемент
            if s[v] < s[u]:  # якщо обраний менше ніж ітеріруємий то це в зворотному напрямку
                u = v  # вибраний елемент стає рівним ітеріруємому
        s[t], s[u] = s[u], s[t]  # та міняє їх місцями

# insertion sort в зворотньому напрямку
def rt(arrayToSort): # застосовуємо функцію
    a = arrayToSort # швидка заміна
    for i in range(len(a)): # діапазон
        v = a[i] # заміна за індексом
        j = i # прирівнюєм значення
        while (a[j - 1] < v) and (j > 0): # поки значення з індексом j-1 більше числа за індексом по ітерації і воно більше 0
            a[j] = a[j - 1] # зменшуємо і направляємось наліво
            j = j - 1 # зменшуємо
        a[j] = v # прирівнюємо знову коли виходимо з циклу
    return a  # повертаємо відсортований список



# Функція для запису часу
def ty(a):

    t = timer()  # таймкр
    a(i)  # аргумент приймає свій аргумент
    c = timer() - t  # час

    print(f'{c} секунд')


if qw == '+':
    if q == '1':
        j(i) # В функцію записуємо замість тимчасового аргументу наше значення, тобто введений список
        ty(j)  # викликаєм функцію для часу
    elif q == '2':
        r(i)
        ty(r)
    else:
        w(i)
        ty(w)

if qw == '-':
    if q == '1':
        we(i)  # В функцію записуємо замість тимчасового аргументу наше значення, тобто введений список
        ty(we)
    elif q == '2':
        er(i)  #В функцію записуємо замість тимчасового аргументу наше значення, тобто введений список
        ty(er)
    else:
        rt(i)  # В функцію записуємо замість тимчасового аргументу наше значення, тобто введений список
        ty(rt)
print(i)
# function=a
# items=b
# elapsed=c


