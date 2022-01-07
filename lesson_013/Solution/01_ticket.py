# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse

template_path = "images/ticket_template.png"
font_path = "SonyEricssonLogo.ttf"

parser = argparse.ArgumentParser()

parser.add_argument('fio', type=str, help='ФИО')
parser.add_argument('from_', type=str, help='Откуда')
parser.add_argument('to', type=str, help='Куда')
parser.add_argument('date', type=str, help='Дата')
parser.add_argument('--save_path', type=str, default=None, help='Путь сохранения')

args = parser.parse_args()
print(args)


def make_ticket(_fio, _from_, _to, _date, _save_path=None):
    ticket = Image.open(template_path)
    draw = ImageDraw.Draw(ticket)
    font = ImageFont.truetype(font_path, size=14)

    fio_pos = (45, 125)
    from_pos = (45, 195)
    to_pos = (45, 260)
    data_pos = (285, 260)

    draw.text(fio_pos, _fio, font=font, fill=ImageColor.colormap['black'])
    draw.text(from_pos, _from_, font=font, fill=ImageColor.colormap['black'])
    draw.text(to_pos, _to, font=font, fill=ImageColor.colormap['black'])
    draw.text(data_pos, _date, font=font, fill=ImageColor.colormap['black'])

    if _save_path:
        ticket.save(_save_path)
        print(f"Файл сохранен в {_save_path}")

    ticket.show()


make_ticket(args.fio, args.from_, args.to, args.date, args.save_path)
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
