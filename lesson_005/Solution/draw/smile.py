import simple_draw as sd


def draw_smile(x, y, color):
    """Ебать серьезный"""
    center_point = sd.get_point(x, y)
    sd.circle(center_point, 100, color, 2)
    left_eye = sd.get_point(x - 50, y + 60)
    sd.circle(left_eye, 10, color, 2)
    right_eye = sd.get_point(x + 50, y + 60)
    sd.circle(right_eye, 10, color, 2)
    nose_start = sd.get_point(x, y + 50)
    nose_stop = sd.get_point(x, y + 10)
    sd.line(nose_start, nose_stop, color, 2)
    mouth_start = sd.get_point(x - 40, y - 50)
    mouth_stop = sd.get_point(x + 40, y - 50)
    sd.line(mouth_start, mouth_stop, color, 2)


if __name__ == '__main__':
    draw_smile(300, 500, sd.COLOR_GREEN)
    sd.pause()
