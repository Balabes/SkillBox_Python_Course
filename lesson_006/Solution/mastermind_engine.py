import random as random_gen

# global hidden_number
hidden_number = ""
try_cnt = 0


def hidden_number_init():
    numbers = ''
    for _ in range(4):
        while True:
            rnd = str(random_gen.randint(0, 9))
            try:
                numbers.index(rnd)
            except ValueError:
                numbers += rnd
                break
            else:
                pass
    return numbers


def check_input(input_string: str):
    result = {'cow': 0, 'bull': 0}
    for ch in input_string:
        index_of_ch = input_string.index(ch)
        try:
            index_in_hidden = hidden_number.index(ch)
        except ValueError:
            break
        else:
            if index_of_ch == index_in_hidden:
                result['bull'] += 1
            else:
                result['cow'] += 1
    return result


if __name__ == '__main__':
    hidden_number = hidden_number_init()
    print('hidden_number = ', hidden_number)
    res = check_input('1234')
    print(f"Быки - {res['bull']}, Коровы - {res['cow']}")
