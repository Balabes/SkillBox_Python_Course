# -*- coding: utf-8 -*-

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import os
import time
import shutil
import zipfile

# from abc import ABCMeta, abstractmethod

src_file = "icons"
aim_folder = "icons_by_year"


class FileSorter():  # да да файловый сортир

    def __init__(self, zip_file_name, result_folder):
        self._zip_file_name = zip_file_name
        self._result_folder = result_folder
        self.work_folder = None
        self.unzip()

    def unzip(self):
        if zipfile.is_zipfile(self._zip_file_name):
            zf = zipfile.ZipFile(self._zip_file_name, 'r')
            self.work_folder = zf.namelist()[0]
            self.work_folder = self.work_folder[:-1]
            zf.extractall()
        else:
            self.work_folder = self._zip_file_name
        # print(self.work_folder)

    def sort_files(self):
        try:
            os.mkdir(path=self._result_folder)
        except FileExistsError:
            pass
        for dirpath, dirnames, filenames in os.walk(self.work_folder):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                file_modified_date = time.gmtime(os.path.getmtime(full_file_path))
                new_path = os.path.join(self._result_folder, str(file_modified_date.tm_year),
                                        str(file_modified_date.tm_mon))
                try:
                    os.makedirs(new_path)
                except FileExistsError:
                    pass
                shutil.copy(full_file_path, new_path)

fs = FileSorter(src_file, aim_folder)
fs.sort_files()
# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
