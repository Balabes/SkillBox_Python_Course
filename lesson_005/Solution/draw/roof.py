import simple_draw as sd
import math


def draw_roof(x, y, length):
    point_start = sd.get_point(x - 100, y)
    length_side = (length + 200) / 1.88 * math.cos(20 / 2 * math.pi)
    v1 = sd.get_vector(start_point=point_start, angle=0, length=length + 200, width=5)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=160, length=length_side, width=5)
    v2.draw()
    v3 = sd.get_vector(start_point=v1.start_point, angle=20, length=length_side, width=5)
    v3.draw()
    return v3.end_point


if __name__ == '__main__':
    draw_roof(100, 100, 100)
    sd.pause()
