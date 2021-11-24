import simple_draw as sd


def draw_trunk(start_point):
    trunk = sd.get_vector(start_point, -90, start_point.y)
    trunk.draw()


def draw_branches(start_point, angle, length):
    if length < 15:
        return

    delta_angle = 20
    angle_right = angle
    angle_left = -(angle + 180)
    next_point_right = next_point_left = start_point
    next_length = length

    brr = sd.get_vector(start_point=next_point_right, angle=angle_right, length=length)
    next_point_right = brr.end_point
    brr.draw()

    next_length *= .65
    next_angle = angle_right + delta_angle
    draw_branches(start_point=next_point_right, angle=next_angle, length=next_length)
    next_angle = angle_right - delta_angle
    draw_branches(start_point=next_point_right, angle=next_angle, length=next_length)

    brl = sd.get_vector(start_point=next_point_left, angle=angle_left, length=length)
    next_point_left = brl.end_point
    brl.draw()

    next_length = length
    next_length *= .65
    next_angle = angle_left + delta_angle
    draw_branches(start_point=next_point_left, angle=next_angle, length=next_length)
    next_angle = angle_right - delta_angle
    draw_branches(start_point=next_point_left, angle=next_angle, length=next_length)


def draw_tree(x, y):
    angle = 140
    length = 150
    start_point = sd.get_point(x, y)
    draw_trunk(start_point)
    draw_branches(start_point, angle, length)


if __name__ == '__main__':
    draw_tree(200, 100)
    sd.pause()
