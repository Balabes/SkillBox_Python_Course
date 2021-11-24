import simple_draw as sd


def draw_sun(x, y, radius):
    center_point = sd.get_point(x, y)
    sd.circle(center_point, radius, sd.COLOR_YELLOW, 0)
    for i in range(16):
        v = sd.get_vector(center_point, 360 * i / 16, 2 * radius, 6)
        v.draw(color=sd.COLOR_YELLOW)


if __name__ == '__main__':
    draw_sun(300, 300, 100)
    sd.pause()
