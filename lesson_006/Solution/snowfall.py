import random as rnd
import simple_draw as sd

N = 20
snowflakes_list = []
screen_x = 1200
screen_y = 800

sd.resolution = (screen_x, screen_y)


def create_snowflakes(n=20):
    snowflakes = []
    for _ in range(n):
        snowflakes.append(
            [rnd.randint(0, screen_x), rnd.randint(screen_y - 200, screen_y), rnd.randint(10, 100), True])
    return snowflakes


def draw_snowflakes(snowflakes, color=sd.COLOR_WHITE):
    for snowflake in snowflakes:
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, length=snowflake[2], color=color)


def get_fallen_snowflakes(snowflakes):
    result = []
    for i, snowflake in enumerate(snowflakes):
        if not snowflake[3]:
            result.append(i)
    return result


def del_snowflakes(snowflakes, death_list):
    for dead_man in death_list:
        del snowflakes[dead_man]


def make_move(snowflakes):
    for snowflake in snowflakes:
        if snowflake[3]:
            if snowflake[1] <= 0:
                snowflake[1] = 0
                snowflake[3] = False
            else:
                snowflake[1] -= 5
    return snowflakes


if __name__ == '__main__':
    snowflakes_list = create_snowflakes()
    print(snowflakes_list)
    draw_snowflakes(snowflakes_list, sd.COLOR_YELLOW)
    sd.pause()
