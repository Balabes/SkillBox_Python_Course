import simple_draw as sd
import random as rnd

screen_x = 600
screen_y = 600

N = 20

snowflakes_list = []


def snowflakes_init():
    for _ in range(N):
        snowflakes_list.append(
            [rnd.randint(0, screen_x), rnd.randint(0, screen_y), rnd.randint(10, 100), True])


def snowflake_fall(snowflakes):
    # while True:
    #     sd.clear_screen()
    for snowflake in snowflakes:
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, length=snowflake[2], color=sd.COLOR_WHITE)
        if snowflake[3]:
            if snowflake[1] <= 0:
                snowflake[1] = rnd.randint(screen_y - 50, screen_y + 50)
            else:
                snowflake[1] -= 5
                snowflake[0] += rnd.randint(-5, 5)


if __name__ == '__main__':
    snowflakes_init()
    snowflake_fall(snowflakes_list)
