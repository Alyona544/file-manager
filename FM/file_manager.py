import os
import shutil

# Получение пути к рабочей папке из файла настроек
def get_working_directory():
    with open('settings.txt', 'r') as f:
        return f.readline().strip()

# Создание папки
def create_folder(name):
    if not os.path.exists(name):
        os.makedirs(name)
        print(f'Папка {name} создана')
    else:
        print(f'Папка {name} уже существует')

# Удаление папки
def delete_folder(name):
    if os.path.exists(name):
        shutil.rmtree(name)
        print(f'Папка {name} удалена')
    else:
        print(f'Папка {name} не существует')

# Перемещение в другую папку
def move_to_folder(name):
    path = os.path.join(get_working_directory(), name)
    if os.path.exists(path):
        os.chdir(path)
        print(f'Вы перешли в папку {name}')
    else:
        print(f'Папка {name} не существует')

# Перемещение вверх на уровень
def move_up():
    os.chdir('..')
    print('Вы перешли на уровень вверх')

# Создание пустого файла
def create_file(name):
    if not os.path.exists(name):
        open(name, 'w').close()
        print(f'Файл {name} создан')
    else:
        print(f'Файл {name} уже существует')

# Запись текста в файл
def write_to_file(name, text):
    if os.path.exists(name):
        with open(name, 'a') as f:
            f.write(text + '\n')
        print(f'Текст успешно записан в файл {name}')
    else:
        print(f'Файл {name} не существует')

# Просмотр содержимого текстового файла
def view_file(name):
    if os.path.exists(name):
        with open(name, 'r') as f:
            print(f.read())
    else:
        print(f'Файл {name} не существует')

# Удаление файла
def delete_file(name):
    if os.path.exists(name):
        os.remove(name)
        print(f'Файл {name} удален')
    else:
        print(f'Файл {name} не существует')

# Копирование файла
def copy_file(src, dst):
    shutil.copy(src, dst)
    print(f'Файл {src} скопирован в {dst}')

# Перемещение файла
def move_file(src, dst):
    shutil.move(src, dst)
    print(f'Файл {src} перемещен в {dst}')

# Переименование файла
def rename_file(src, dst):
    os.rename(src, dst)
    print(f'Файл {src} переименован в {dst}')

# Основной цикл программы
def main():
    while True:
        command = input('\nВведите команду:\n'
                        '- create_folder\n'
                        '- delete_folder\n'
                        '- move_to_folder\n'
                        '- move_up\n'
                        '- create_file\n'
                        '- write_to_file\n'
                        '- view_file\n'
                        '- delete_file\n'
                        '- copy_file\n'
                        '- move_file\n'
                        '- rename_file\n'
                        '- exit\n').split()
        if command[0] == 'create_folder':
            create_folder(command[1])
        elif command[0] == 'delete_folder':
            delete_folder(command[1])
        elif command[0] == 'move_to_folder':
            move_to_folder(command[1])
        elif command[0] == 'move_up':
            move_up()
        elif command[0] == 'create_file':
            create_file(command[1])
        elif command[0] == 'write_to_file':
            write_to_file(command[1], command[2])
        elif command[0] == 'view_file':
            view_file(command[1])
        elif command[0] == 'delete_file':
            delete_file(command[1])
        elif command[0] == 'copy_file':
            copy_file(command[1], command[2])
        elif command[0] == 'move_file':
            move_file(command[1], command[2])
        elif command[0] == 'rename_file':
            rename_file(command[1], command[2])
        elif command[0] == 'exit':
            break

if __name__ == '__main__':
    main()

    '''Примеры команд:
- create_folder folder1 - создает папку с именем folder1
- delete_folder folder1 - удаляет папку с именем folder1
- move_to_folder folder1 - переходит в папку с именем folder1
- move_up - переходит на уровень вверх
- create_file file1.txt - создает пустой файл с именем file1.txt
- write_to_file file1.txt Hello, world! - записывает в файл file1.txt текст Hello, world!
- view_file file1.txt - выводит содержимое файла file1.txt
- delete_file file1.txt - удаляет файл file1.txt
- copy_file file1.txt folder1 - копирует файл file1.txt в папку folder1
- move_file file1.txt folder1 - перемещает файл file1.txt в папку folder1
- rename_file file1.txt new_file.txt - переименовывает файл file1.txt в new_file.txt
- exit - завершает выполнение программы'''