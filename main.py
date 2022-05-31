#! python3
# backup_to_ZIP.py - Копирует папку со всем его содержимым в zip-файл с инкрементируемым номером копии в имени файла

import zipfile, os

def backup_to_zip(folder):
    """Создает резервную копию всего содержимого файла Folder в виде Zip-файла"""
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zip_filename = f"{os.path.basename(folder)}_{str(number)}.zip"
        if not os.path.exists(zip_filename):
            break
        number += 1

    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Добавление файлов из папки {foldername}")
        # Добавить в zip-файл текущую папку
        backup_zip.write(foldername)
        # Добавить в zip-файл все файлы из данной папки
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()

if __name__ == '__main__':
    ...