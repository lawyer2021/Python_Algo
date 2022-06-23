# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):  # класс для ветвей дерева - внутренних узлов; у них есть потомки
    def walk(self, code, step):
        self.left.walk(code, step + "0")  # пойти в левого потомка, добавив к префиксу "0"
        self.right.walk(code, step + "1")  # затем пойти в правого потомка, добавив к префиксу "1"


class Leaf(namedtuple("Leaf", ["char"])):  # класс для листьев дерева, у него нет потомков, но есть значение символа
    def walk(self, code, step):
        # потомков у листа нет, по этому для значения мы запишем построенный код для данного символа
        code[
            self.char] = step or "0"  # если строка длиной 1 то step = "", для этого случая установим значение step = "0"


def huffman_encode(s):  # функция кодирования строки в коды Хаффмана
    h = []  # создаем очередь с приоритетами
    for ch, freq in Counter(s).items():  # строим очередь с помощью цикла, добавив счетчик, уникальный для всех листьев
        h.append((freq, len(h), Leaf(ch)))  # очередь будет представлена частотой символа, счетчиком и самим символом
    heapq.heapify(h)  # строим очередь с приоритетами
    count = len(h)  # инициализируем значение счетчика с длиной равной длине очереди
    while len(h) > 1:  # пока в очереди есть хотя бы 2 элемента
        freq1, _count1, left = heapq.heappop(h)  # вытащим элемент с минимальной частотой - левый узел
        freq2, _count2, right = heapq.heappop(h)  # вытащим следующий элемент с минимальной частотой - правый узел
        # поместим в очередь новый элемент, у которого частота равна сумме частот вытащенных элементов
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))  # добавляем новый внутренний узел у которого
        # потомки left и right соответственно
        count += 1  # увеличиваем значение счетчика при добавлении нового элемента дерева
    code = {}  # создаем словарь кодов символов
    if h:  # если строка пустая, то очередь будет пустая и обходить нечего
        [(_freq, _count, root)] = h  # в очереди 1 элемент без приоритета, а сам элемент - корень дерева
        root.walk(code, "")  # обходим дерево от корня и заполняем словарь для получения кодирования Хаффмана
    return code  # возвращаем словарь символов и соответствующих им кодов


my_string = "Python Data Structures"
code = huffman_encode(my_string)
for i in my_string:
    huffman = ' '.join(code[i] for i in my_string)
print("Python Data Structures = ", huffman, '\nCловарь символов:')
for key, value in code.items():
    print("{0}: {1}".format(key, value))