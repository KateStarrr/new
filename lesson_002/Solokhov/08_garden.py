#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
<<<<<<< HEAD
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set = set(meadow)
=======
garden_set = set(garden)
meadow_set = set(meadow)
print(garden_set, meadow_set)


>>>>>>> 341e0f52f6cc9049d8719f58db8a521275f5857a

# выведите на консоль все виды цветов
print(garden_set | meadow_set)

# выведите на консоль те, которые растут и там и там
print(garden_set & meadow_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
print(garden_set - meadow_set)

# выведите на консоль те, которые растут на лугу, но не растут в саду
print(meadow_set - garden_set)
<<<<<<< HEAD


=======
>>>>>>> 341e0f52f6cc9049d8719f58db8a521275f5857a
