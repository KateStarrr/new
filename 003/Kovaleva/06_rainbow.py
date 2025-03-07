# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start1, start2 = 50, 50
end1, end2 = 350, 450
step = 5
for i in range (0, 7):
    a = i * step
    start1 += a
    start2 += a
    end1 += a
    end2 += a
    sd.line(start_point = sd.get_point(start1, start2), end_point = sd.get_point(end1, end2), color = rainbow_colors[i], width = 4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


sd.pause()
