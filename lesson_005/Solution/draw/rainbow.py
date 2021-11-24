import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def draw_rainbow(colors_list, x, y, radius, step):
    start_point = sd.get_point(x, y)
    for color in colors_list:
        radius += step
        sd.circle(start_point, radius, color, 10)


if __name__ == '__main__':
    draw_rainbow(rainbow_colors, 300, 0, 90, 10)
    sd.pause()
