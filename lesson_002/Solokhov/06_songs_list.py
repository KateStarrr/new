#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

<<<<<<< HEAD
<<<<<<< HEAD
cost = violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[8][1]
print("Три песни звучат", cost, "минут")
=======
=======
>>>>>>> 9e4ea4dcc8a4f845909ef8fcd064ff92e9055da8
sum1 = violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[8][1]
print('Три песни звучат', round(sum1, 2), 'минут')


<<<<<<< HEAD
>>>>>>> 341e0f52f6cc9049d8719f58db8a521275f5857a
=======
=======
cost = violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[8][1]
print("Три песни звучат", cost, "минут")
>>>>>>> 12eef8ccb11bebf8d2c24e207d99da6575481a28
>>>>>>> 9e4ea4dcc8a4f845909ef8fcd064ff92e9055da8
# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут
<<<<<<< HEAD
<<<<<<< HEAD
cost = violator_songs_dict['Sweetest Perfection'] + violator_songs_dict['Policy of Truth'] + violator_songs_dict['Blue Dress']
print("А другие три песни звучат", cost, "минут")

=======

sum2 = violator_songs_dict[1][1] + violator_songs_dict[6][1] + violator_songs_dict[7][1]
print('А другие три песни звучат', round(sum2, 2), 'минут')
>>>>>>> 341e0f52f6cc9049d8719f58db8a521275f5857a
=======

sum2 = violator_songs_dict[1][1] + violator_songs_dict[6][1] + violator_songs_dict[7][1]
print('А другие три песни звучат', round(sum2, 2), 'минут')
=======
cost = violator_songs_dict['Sweetest Perfection'] + violator_songs_dict['Policy of Truth'] + violator_songs_dict['Blue Dress']
print("А другие три песни звучат", cost, "минут")

>>>>>>> 12eef8ccb11bebf8d2c24e207d99da6575481a28
>>>>>>> 9e4ea4dcc8a4f845909ef8fcd064ff92e9055da8
