import os
import time

directory = r'C:\Users\Александр\PycharmProjects\PythonDeveloper---UrbanUnivercity'

for root, dirs, files in os.walk(directory, topdown=True):
    for file in files:
        file_path = os.path.join(root,file)
        file_size = os.path.getsize(file_path)
        parent_dir = root
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file_path)))
        print(f'Файл: {file} Путь: {file_path}, Размер: {file_size}, Изменен: {formatted_time}, Папка: {parent_dir}')
