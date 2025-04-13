# Лабораторные работы по Python

## Файлы с кодом
- [Лаба-1 в1.py](https://github.com/gulidovalera/Maksimuk_Uladzislau_Python_Labs/blob/Lab_1/Lab%201.py) - Лабораторная работа 1
- [лаба2 (1).py](https://github.com/gulidovalera/laba/blob/лаба-1/Python/лаба2%20(1).py) - Лабораторная работа 2
- [В3задание2(2).py](https://github.com/gulidovalera/laba/blob/лаба-1/Python/%23В3задание2(2).py), [В1задание1(2).py](https://github.com/gulidovalera/laba/blob/лаба-1/В1задание1(2).py) - Лабораторная работа 3
- [лаба4_В3 биопитон с окном для файла.py](https://github.com/gulidovalera/laba/blob/лаба-1/Python/лаба4_В3%20биопитон%20с%20окном%20для%20файла.py) - Лабораторная работа 4

---

## Лабораторная работа 1: "Подсчёт точечных мутаций методом Хэмминга для триплетов ДНК"

### Цель работы
Исследование точечных мутаций в последовательностях ДНК путём вычисления расстояния Хэмминга между триплетами (группами из трёх нуклеотидов) двух гомологичных цепей ДНК. Разработка программных реализаций на Python для решения данной задачи.

## Задачи
1. Реализовать функцию для вычисления расстояния Хэмминга между триплетами двух последовательностей ДНК
2. Создать объектно-ориентированную версию программы с использованием класса
3. Обеспечить корректную обработку входных данных:
  - Проверка равенства длин последовательностей
  - Валидация допустимых символов (A, T, G, C)
4. Протестировать программу на примере из условия задачи

### Инструменты и алгоритмы
 Язык программирования: Python.
 Стандартные библиотеки Python (без дополнительных зависимостей)
 Функциональная реализация:
 - Разбиение последовательностей на триплеты с шагом 3
 - Поэлементное сравнение нуклеотидов в соответствующих триплетах
 - Подсчёт количества несовпадений
Объектно-ориентированная реализация:
 - Класс HammingTripletCalculator, инкапсулирующий:
  - Хранение последовательностей
  - Ввод данных
  - Вычисление расстояния Хэмминга
  - Использование метода zip для попарного сравнения символов
Структура программы:
 ```python
# Функциональный подход
def hamming_distance_triplets(s, t):
    # ... реализация ...

# Объектно-ориентированный подход
class HammingTripletCalculator:
    def __init__(self): ...
    def input_sequence(self): ...
    def calculate_distance(self): ...
 ```

### Ошибки и исправления
Проблема: Отсутствие проверки длины последовательностей
Симптомы: Неверные результаты при неравных длинах
Решение: Добавить проверку if len(s) != len(t): raise ValueError()

Проблема: Нет валидации входных символов
Симптомы: Возможны ошибки при вводе недопустимых символов
Решение: Добавить проверку символов на принадлежность к {'A', 'T', 'G', 'C'}

Проблема: Неполные триплеты в конце последовательности
Симптомы: Потеря данных при длине не кратной 3
Решение: Обрабатывать остаток как отдельный триплет или требовать длину, кратную 3

Проблема: Чувствительность к регистру
Симптомы: Разные результаты для 'A' и 'a'
Решение: Приводить последовательности к верхнему регистру

### Выводы
Разработаны две реализации алгоритма подсчёта расстояния Хэмминга для триплетов ДНК:
 - Процедурная (функциональная) версия
 - Объектно-ориентированная версия

Программа успешно решает поставленную задачу:
 - Корректно вычисляет количество точечных мутаций
 - Работает с последовательностями длиной до 1000 символов
 - Обрабатывает триплеты как отдельные блоки сравнения

Объектно-ориентированный подход показал следующие преимущества:
 - Лучшая структурированность кода
 - Инкапсуляция данных и методов
 - Возможность легкого расширения функциональности

Практическое применение:
 - Анализ мутаций в кодирующих областях ДНК
 - Сравнение гомологичных последовательностей
 - Исследование эволюционных расстояний между видами

Дальнейшие улучшения могут включать:
 - Визуализацию различий между последовательностями
 - Статистический анализ распределения мутаций
 - Поддержку других типов нуклеиновых кислот (РНК)
 - Расширение для работы с аминокислотными последовательностями

Программа демонстрирует эффективный подход к анализу точечных мутаций и может служить основой для более сложных биоинформатических инструментов.

---

## Лабораторная работа 2: "Анализ мотивов ДНК методом поиска подстрок"

### Цель работы
Разработка программы для поиска всех вхождений заданного мотива (короткой последовательности ДНК) в геномной последовательности с определением точных позиций вхождения и их последующей сортировкой.

### Задачи
1. Реализовать алгоритм поиска подстроки в строке ДНК
2. Обеспечить обработку входных данных:
 - Проверка длины последовательностей
 - Нормализация регистра символов
 - Валидация нуклеотидных последовательностей
3. Реализовать сортировку найденных позиций с использованием алгоритма сортировки слиянием
4. Протестировать программу на примере из условия задачи
   
### Инструменты и алгоритмы
- Язык программирования: Python.
- Стандартные библиотеки Python
####Основные алгоритмы:
Алгоритм поиска подстроки:
 - Последовательный перебор всех возможных подстрок
 - Сравнение с искомым мотивом
 - Сложность O(n*m), где n - длина геномной последовательности, m - длина мотива
Алгоритм сортировки слиянием:
 - Рекурсивное разделение массива
 - Слияние упорядоченных подмассивов
 - Сложность O(n log n)
    ```python
   def find_positions(s, t):  # Поиск позиций
    # ... реализация ...
   def merge_sort(arr):  # Сортировка слиянием
    # ... реализация ...
   def merge(left, right):  # Слияние подмассивов
    # ... реализация ...
    
    ```

### Ошибки и исправления
Проблема: Чувствительность к регистру символов
Решение: Приведение последовательностей к верхнему регистру (s.upper(), t.upper())
Проблема: Некорректная обработка граничных условий

Решение: Добавление проверок:

 ```python
if len(t) == 0 or len(t) > len(s):
    return positions
 ```
Проблема: Избыточная сортировка уже упорядоченных данных
Анализ: Позиции при поиске сохраняются в порядке возрастания
Решение: Можно исключить сортировку или оставить для универс

### Выводы
Разработанная программа успешно решает поставленную задачу поиска мотивов в последовательностях ДНК:
 - Корректно находит все вхождения подстроки
 - Обрабатывает последовательности длиной до 1 кб
 - Обеспечивает вывод результатов в требуемом формате

Реализованы два ключевых алгоритма:
 - Наивный алгоритм поиска подстроки
 - Эффективный алгоритм сортировки слиянием

Обнаруженные проблемы и их решения:
 - Учтена регистрозависимость
 - Добавлены проверки граничных условий
 - Оптимизирован процесс сортировки

Практическое применение:
 - Анализ геномных последовательностей
 - Поиск регуляторных элементов
 - Идентификация повторяющихся участков ДНК

Перспективы развития:
 - Реализация более эффективных алгоритмов поиска (Кнута-Морриса-Пратта)
 - Добавление поддержки неточных совпадений
 - Визуализация результатов поиска
 - Интеграция с биоинформатическими базами данных
---

## "Лабораторная работа №3 ПРЕДСТАВЛЕНИЕ ДАННЫХ В PYTHON"

### Цель работы
Освоение методов визуализации данных в Python с использованием библиотеки matplotlib и дополнительных инструментов (seaborn, statsmodels):
1. Построение диаграммы рассеяния для анализа взаимосвязи между признаками с цветовой дифференциацией классов.
2. Создание графиков временных рядов для изучения динамики изменений данных.

### Задания

Задание 1. Диаграмма рассеяния

- Загрузить данные о курении и заболеваемости раком в Китае.
- Разделить регионы на две группы (A-R и S-Z) по первой букве названия.

Построить диаграмму рассеяния:
- Ось X: число курящих с раком.
- Ось Y: число некурящих с раком.
- Цвет маркеров: группа региона.
- Настроить оформление (заголовок, подписи осей, легенду, сетку).

Задание 2. График временных рядов

- Загрузить данные о стоке реки Нил.
- Отфильтровать данные за период 1870–1910 гг.

Построить график динамики:
- Ось X: год.
- Ось Y: объём стока (м³/с).
- Добавить маркеры и линейный тренд.
- Настроить шкалу времени (метки каждые 5 лет) и визуальные элементы.

### Инструменты

####Библиотеки:
matplotlib.pyplot — базовые функции визуализации.
seaborn — улучшенные стили графиков (для диаграммы рассеяния).
statsmodels.datasets — загрузка стандартных наборов данных (Китай, Нил).
pandas — обработка и фильтрация данных.

####Алгоритмы:
Для диаграммы рассеяния:
 - Группировка регионов через lambda-функцию.
 - Использование sns.scatterplot с параметрами:

 ```python
hue='Location_Group',  # Цвет по группе
palette=['navy', 'crimson'],  # Цвета маркеров
s=80,  # Размер точек
edgecolor='black'  # Обводка
Добавление сетки и легенды.
 ```

Для временного ряда:
 - Фильтрация данных по году:

```python
filtered_data = data[(data['year'] >= 1870) & (data['year'] <= 1910)]
Построение линии тренда с маркерами:
```
```python
plt.plot(..., marker='o', linestyle='-', linewidth=1.5)
Настройка оси X с шагом 5 лет:
```
```python
plt.xticks(range(1870, 1911, 5))
```

### Ошибки и исправления

Проблема: Некорректное отображение данных за 1870 год (отсутствие в dataset).
Решение: Проверка на пустоту filtered_data и сдвиг диапазона на 1871–1910.
Проблема: Наложение подписей на диаграмме рассеяния.

Решение: Увеличение размера графика (figsize=(12, 7)).
Проблема: Слишком частые метки на оси X временного ряда.
Решение: Установка шага в 5 лет через plt.xticks().

Проблема: Нечитаемые цвета маркеров.
Решение: Использование контрастной палитры (navy и crimson).

### Выводы
Результаты задания 1:
 - Диаграмма рассеяния выявила слабую корреляцию между числом курящих и некурящих больных раком.
 - Разделение на группы A-R и S-Z не показало значимых кластеров, что требует дополнительного анализа.

Результаты задания 2:
- График стока Нила демонстрирует значительные колебания с пиками в 1878 и 1892 гг., что может быть связано с климатическими изменениями.
- Линейный тренд не выявлен, данные носят случайный характер.

Общие выводы:
- Библиотеки matplotlib и seaborn предоставляют гибкие инструменты для визуализации.
- Для временных рядов критична настройка шкалы времени и фильтрация данных.
- Цветовая дифференциация улучшает восприятие многомерных данных.

---
