#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = '"Терминатор", "Пятый элемент", "Аватар", "Чужие", "Назад в будущее"'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
print(my_favorite_movies[51:66])
print(my_favorite_movies[42:47])
print(my_favorite_movies[32:38])
print(my_favorite_movies[1:11])
