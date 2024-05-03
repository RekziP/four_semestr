import os
from lib import FileManager


def print_help():
    print("Список доступных команд:")
    print("  create_dir <название_директории>: Создать новую папку")
    print("  delete_dir <название_директории>: Удалить существующую папку")
    print("  navigate <название_директории>: Перейти в папку")
    print("  create_file <название_файла>: Создать файл")
    print("  read_file <название_файла>: Отобразить содержимое файла")
    print("  write_file <название_файла>: Записать в файл")
    print("  copy_file <исходный_файл> <целевой_файл>: Копировать файл")
    print("  move_file <исходный_файл> <целевой_файл>: Переместить файл")
    print("  rename_file <текущее_название_файла> <новое_название_файла>: Переименовать файл")
    print("  exit: Выйти из менеджера файлов")


if __name__ == "__main__":
    work_dir = os.getcwd()
    file_manager = FileManager(work_dir)
    commands = {
        'help': 'help',
        'exit': 'exit',
        'create_dir': lambda arg: file_manager.create_directory(arg),
        'delete_dir': lambda arg: file_manager.delete_directory(arg),
        'navigate': lambda arg: file_manager.navigate(arg),
        'create_file': lambda arg: file_manager.create_file(arg),
        'read_file': lambda arg: file_manager.read_file(arg),
        'write_file': lambda args: file_manager.write_file(*args.split(maxsplit=1)),
        'copy_file': lambda args: file_manager.copy_file(*args.split(maxsplit=1)),
        'move_file': lambda args: file_manager.move_file(*args.split(maxsplit=1)),
        'rename_file': lambda args: file_manager.rename_file(*args.split(maxsplit=1))
    }

    while True:
        print("\nТекущая директория:", file_manager.current_directory)
        command = input("Введите команду (напишите 'help', чтобы увидеть доступные команды): ").strip().lower()

        if command in commands:
            if command == 'exit':
                print("Выход из файлового менеджера")
                break
            if command == 'help':
                print_help()
            else:
                args = input("Введите аргумент(ы): ").strip()
                commands[command](args)
        else:
            print("Несуществующая команда. Напишите 'help', чтобы увидеть доступные команды")
