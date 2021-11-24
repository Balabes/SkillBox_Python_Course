import simple_draw as sd

sd.resolution = (800, 800)


def draw_wall(x_start, y_start, x_stop, y_stop):
    y = y_start - 50

    brick_height = 50
    brick_width = 100

    row_count = (y_stop - y_start) // brick_height
    column_count = (x_stop - x_start) // brick_width

    point_0 = sd.get_point(x_start, y_start)
    v1 = sd.get_vector(start_point=point_0, angle=90, length=row_count * brick_height, width=5)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=0, length=column_count * brick_width, width=5)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=270, length=row_count * brick_height, width=5)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=180, length=column_count * brick_width, width=5)
    v4.draw()

    for i in range(row_count):
        y += brick_height
        start_point = sd.get_point(x_start, y)
        stop_point = sd.get_point(x_stop, y)
        sd.line(start_point, stop_point, sd.COLOR_YELLOW, 1)
        if i % 2 == 0:
            x = x_start - 100
            for _ in range(column_count):
                x += brick_width
                start_point = sd.get_point(x, y)
                stop_point = sd.get_point(x, y + brick_height)
                sd.line(start_point, stop_point, sd.COLOR_YELLOW, 1)
        if i % 2 != 0:
            x = x_start - 50
            for _ in range(column_count):
                x += brick_width
                start_point = sd.get_point(x, y)
                stop_point = sd.get_point(x, y + brick_height)
                sd.line(start_point, stop_point, sd.COLOR_YELLOW, 1)


if __name__ == '__main__':
    draw_wall(x_start=400, y_start=10, x_stop=800, y_stop=410)
    sd.pause()
