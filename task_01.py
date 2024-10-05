import os
import shutil 
import sys

# Функція для рекурсивного копіювання файлів
def copy_files_recursively(src, dest):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)  
        if os.path.isdir(src_path):
            copy_files_recursively(src_path, dest)
        else:
            file_extension = os.path.splitext(item)[1].lower()  
            target_dir = os.path.join(dest, file_extension[1:])  
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)  
            try:
                shutil.copy2(src_path, target_dir)
                print(f"Файл {item} успішно скопійовано в {target_dir}")
            except Exception as e:
                print(f"Помилка під час копіювання файлу {item}: {e}")

# Головна функція для запуску програми
def main():
    # Перевіряємо аргументи командного рядка
    if len(sys.argv) < 2:
        print("Вкажіть шлях до вихідної директорії!")
        return
    src_dir = sys.argv[1]  
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'  
    # Перевірка, чи існує вихідна директорія
    if not os.path.exists(src_dir):
        print(f"Вихідна директорія {src_dir} не існує!")
        return
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Викликаємо функцію для рекурсивного копіювання файлів
    copy_files_recursively(src_dir, dest_dir)
    print("Робота завершена!")

if __name__ == "__main__":
    main()
