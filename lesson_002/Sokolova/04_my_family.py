#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mama', 'papa', 'brat']


# список списков приблизителного роста членов вашей семьи
my_family_height = [['mama', 180], ['papa', 175], ['brat', 183]]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
p = my_family_height[1][1]
m = my_family_height[0][1]
b = my_family_height[2][1]

print ('Рост отца -', p)

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print ('Общий рост моей семьи -', p + m + b)