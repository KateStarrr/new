#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Мама","Папа","Сестра","Я"]
# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ["Мама",164],
    ["Папа",189],
    ["Сестра",90],
    ["Я",188]
    ]

print('Рост отца -', my_family_height[1][1], 'см')#строка-столбец
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
summ = 0
for a  in my_family_height:
    summ += a[1]
print('Общий рост моей семьи -', summ, 'см')