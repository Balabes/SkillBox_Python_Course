class InvalidChar(Exception):
    pass


x_list = ['x', 'X']


def game_result_parser(game_result):
    points = 0
    i = 0
    length = len(game_result)
    input_string = str(game_result)
    while i < length:
        if input_string[i] in x_list:
            points += 20
        elif input_string[i].isdigit():
            if input_string[i + 1] == '/':
                points += 15
                i += 1
            elif input_string[i + 1] == '-':
                points += int(input_string[i])
                i += 1
            else:
                points += int(input_string[i])
                points += int(input_string[i + 1])
                i += 1
        elif input_string[i] == '-':
            if input_string[i + 1] == '/':
                points += 15
                i += 1
            elif input_string[i+1].isdigit():
                points += int(input_string[i+1])
                i += 1
            else:
                i += 1
        else:
            raise InvalidChar("Invalid char in result")
        i += 1

    print(input_string)
    print(points)
    return points
