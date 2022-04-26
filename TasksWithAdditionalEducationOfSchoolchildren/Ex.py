#Будем называть 2 числа родственными, если чётные цифры у них
#одинаковы и стоят в одном и том же порядке, при этом нечётные
#цифры роли не играют. Например, числа 18104 и 93807743
#родные, а 18104 и 10418 – нет. Числа, не содержащие чётных
#цифр, родственными не являются. Разработайте программу,
#получающую на вход натуральные числа (по одному в строке,
#конец ввода по пустой строке) и выводящую все числа,
#родственные первому введённому числу, в порядке возрастания.

a = []
while True:
    try:
        data = int(input())
        a.append(data)
    except ValueError: break
c1 = list(map(int, str(a[0])))
c2 = []
c3 = []
c4 = []
for k in range(len(c1)):
    if c1[k] % 2 == 0:
        c2.append(c1[k])
for i in range(1, len(a)):
    c = list(map(int, str(a[i])))
    for ii in range(len(c)):
        if ((c[ii] % 2 == 0) or (c[ii] == 0)):
            c3.append(c[ii])
        else:
            continue
    if (len(c3) == 0):
        continue
    elif c2 ==c3:
        c4.append(a[i])
        c3 = []
    else:
        c3 = []
    c4.sort()
print(c4)






def kill(n):
    for b in "13579":
        n = n.replace(b, "")
    return n
n = kill(input())
r = []
while True:
    s = input()
    if s =='':
        break
    if kill(s) == n:
        r.append(int(s))
print(*sorted(r))





#Делфтский яблокоед всегда радуется, когда съедаемое им яблоко больше,
# чем то яблоко, которое он съел перед этим.
#У вас есть N яблок. Известен вес каждого Vi, i=1..N.
# Сколько раз обрадуется ДЯ в ходе поедания ваших яблок,
#если вы переложите их в оптимальной для ДЯ последовательности?

#Входные данные: в первой строке натуральное число N<=100 – количество яблок,
#во второй N натуральных чисел, разделённых пробелами – веса яблок.
#Выходные данные: Целое число - количество радостей яблокоеда.

N=int(input())
count = 1
l = [int(z) for y, z in enumerate(input().split()) if N <=100 and z.isdigit()][:N]
print(l)
zmax=l[0]
for i in range(len(l) -1):
    if l[i+1] > l[i]:
        count +=1
print(count)





from collections import Counter
n = int(input())
y = list(map(int, input().split()))
d = Counter(y)
r = len(d) - 1
for j in range(2, n+1):
    c = 0
    for q in d:
        if d[q]>= j:
            c +=1
    if c > 1:
        r += c - 1
print(r)






#В криптоанализе широко применяют частотные таблицы символов в языке.
#Попробуем построить такую таблицу для введённой строки. Пример вывода - вот.
#Как видите, символы в таблице упорядочены по убыванию частоты.

#Эту задачу можно решить разными способами - годится любой,
#не слишком громоздкий. Одно из возможных решений использует и словари, и списки, и множество.

# со словарем
a = input()
lst = list(a)
d = dict()
for i in range(len(a)):
    d[lst[i]] = [lst.count(lst[i])]
d = dict(sorted(d.items(), key=lambda x: x[1], reverse = True))
for keys,values in d.items():
    print(keys + '  ' + str(*values))


# с множеством
s = input().lower()
ls = list(set(s))
pc = [s.count(str(ls[i])) for i in range(len(ls))]
a = list(zip(ls,pc))
lst = [a[i] for i in range(len(a))]
lst.sort(key = lambda x: -(x[1]))
for i in range(len(lst)):
    print(str(lst[i][0]) + '      ' + str(lst[i][1]))


# со списками
a = list(input("Введите строку - ").lower())
res_a = []
res_v = []

for i in a:
    if i not in res_a:
        res_v.append(int(a.count(i)))
        res_a.append(i)

res = list(zip(res_a, res_v))
res.sort(key = lambda x:x[1], reverse=True)
for i in range(len(res)):
    print(str(res[i][0]) + '      ' + str(res[i][1]))


#Есть строка, каждый игрок "откусывает" часть "сосиски" либо один элемент,
#либо два, в зависимости как удачно игрок выберет
#В конце игры программа сообщает результат, например: Вы выиграли 521 : 417

#Первым ходит пользователь. Стратегия компьютера - на ваше усмотрение.

from random import randint as R
from collections import deque
print("====================== Игра 'СОСИСКА' =====================")
print('Цель - откусывая по очереди с компом слева или справа\nнаесть как можно большую сумму.')
ss = deque(R(10, 99) for i in range(R(5, 30)*2))
number_of_round = 1
comp = 0
user = 0
print("!!! Комп начинает и не проигрывает при любой сосиске! !!!")
n = 0
s1 = sum(ss[i] for i in range(0,len(ss),2))
s2 = sum(ss[i] for i in range(1,len(ss),2))
h = 1 if s1 >= s2 else 2
while len(ss) != 0:
    print("\nСОСИСКА: ", " ".join(str(x) for x in ss))
    if n == 0:
        print("Ход 1 - Комп:", h)
        if h == 1:
            comp += ss.popleft()
        else:
            comp += ss.pop()
    elif n % 2 == 1:
        u = int(input("Ход " + str(n + 1) + "- Юзер (1-откусить слева, 2 - справа: "))
        if u == 1:
            user += ss.popleft()
        else:
            user += ss.pop()
    else:
        h = u
        print("Ход", n, "- Комп:", h)
        if h == 1:
            comp += ss.popleft()
        else:
            comp += ss.pop()
    print("Комп:", comp, ", Юзер:", user)
    n += 1
if comp == user:
    print("Фигасе - ничья!")
else:
    print("Комп таки победил. А вы ждали чего-то другого?")





#На числовой прямой расположены N различных точек с номрами от 1 до N.
# Расстояния между любыми двумя точками известны и заданы в виде таблицы.
# Требуется определить номера двух крайних точек и вывести их в порядке возрастания.
#Входные данные: в первой строке – количество точек N, 2≤N≤50,
# далее – N строк по N разделённых пробелами натуральных чисел, не превосходящих 1000 - расстояния
# между точками: в строке с номером Х на позиции Y (нумерация с 1) находится расстояние
# между точками с номерами X и Y. Корректность данных гарантируется.
#Выходные данные: строка, содержащая 2 натуральных числа, номера крайних точек в порядке возрастания.
#Для отправки решений необходимо выполнить вход.
n = int(input())
mx = 0
for i in range(n):
    q = list(map(int, input().split()))
    for j in range(n):
        if q[j] > mx:
            mx = q[j]
            mi = i
            mj = j
mi, mj = min(mi, mj) + 1, max(mi, mj) + 1
print(mi, mj)




# Что должна делать программа, ясно из картинки.
# На вход подаётся натуральное число N, не превышающее 9.
# Выводится вот такой вот «фонарик», впритирку к левому краю консоли,
# все строки одинаковой длины. В центре фонарика - N.
n = int(input())
for i in range(2 * n - 1):
    q = abs(n - i - 1)
    p = 2 * n - 1 - 2 * q
    s = ' ' * q
    for j in range(1, p // 2 + 2):
        s += str(j)
    for j in range(p//2, 0, -1):
        s += str(j)
    s += ' ' * q
    print(s)
