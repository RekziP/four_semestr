import os
import shutil

class FileManager:
    def __init__(self, working_directory):
        # Инициализация рабочей директории
        self.working_directory = working_directory
        self.current_directory = working_directory

    def create_directory(self, directory_name):
        # Создание новой директории
        new_directory_path = os.path.join(self.current_directory, directory_name)
        if os.path.exists(new_directory_path):
            print(f"Директория '{directory_name}' уже существует в текущей директории")
        else:
            os.makedirs(new_directory_path)
            print(f"Директория '{directory_name}' успешно создана")

    def delete_directory(self, directory_name):
        # Удаление директории
        directory_path = os.path.join(self.current_directory, directory_name)
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)
            print(f"Директория '{directory_name}' успешно удалена")
        else:
            print(f"Директория '{directory_name}' не найдена в текущей директории")

    def navigate(self, directory_name):
        # Изменение текущей рабочей директории
        new_directory = os.path.join(self.current_directory, directory_name)
        if os.path.isdir(new_directory):
            if os.path.abspath(new_directory).startswith(os.path.abspath(self.working_directory)):
                self.current_directory = new_directory
                print(f"Текущая директория изменена на '{self.current_directory}'.")
            else:
                print(f"Доступ запрещен: '{new_directory}' находится за пределами рабочей директории")
        else:
            print(f"Директория '{directory_name}' не найдена в '{self.current_directory}'.")

    def create_file(self, file_name):
        # Создание нового файла
        try:
            with open(os.path.join(self.current_directory, file_name), 'w') as file:
                print(f"Файл '{file_name}' успешно создан")
        except FileExistsError:
            print(f"Файл '{file_name}' уже существует")

    def read_file(self, file_name):
        # Прочитать содержимое файла
        try:
            with open(os.path.join(self.current_directory, file_name), 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден")

    def write_file(self, file_name, content):
        # Записать в файл
        with open(os.path.join(self.current_directory, file_name), 'w') as file:
            file.write(content)
            print(f"Содержимое записано в '{file_name}' успешно")

    def copy_file(self, source_file, destination_file):
        # Скопировать файл
        source_path = os.path.join(self.current_directory, source_file)
        destination_path = os.path.join(self.current_directory, destination_file)
        try:
            shutil.copy(source_path, destination_path)
            print(f"Файл '{source_file}' скопирован в '{destination_file}' успешно")
        except FileNotFoundError:
            print(f"Файл '{source_file}' не найден")
        except FileExistsError:
            print(f"Файл '{destination_file}' уже существует")

    def move_file(self, source_file, destination_file):
        # Переместить файл
        source_path = os.path.join(self.current_directory, source_file)
        destination_path = os.path.join(self.current_directory, destination_file)
        try:
            shutil.move(source_path, destination_path)
            print(f"Файл '{source_file}' перемещен в '{destination_file}' успешно")
        except FileNotFoundError:
            print(f"Файл '{source_file}' не найден")
        except FileExistsError:
            print(f"Файл '{destination_file}' уже существует")

    def rename_file(self, current_file, new_file_name):
        # Переименовать файл
        current_path = os.path.join(self.current_directory, current_file)
        new_path = os.path.join(self.current_directory, new_file_name)
        try:
            os.rename(current_path, new_path)
            print(f"Файл '{current_file}' переименован в '{new_file_name}' успешно")
        except FileNotFoundError:
            print(f"Файл '{current_file}' не найден")
        except FileExistsError:
            print(f"Файл '{new_file_name}' уже существует")

