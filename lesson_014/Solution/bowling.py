def game_result_parser(game_result):
    points = 0
    input_string = game_result
    for char in input_string:
        if char == 'x' or char == 'X':
            points += 20
        elif char == '/':
            points += 15

    print(input_string)
