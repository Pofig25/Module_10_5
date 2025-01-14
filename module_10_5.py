import time                                                     # Импортируем модуль для измерения времени
from multiprocessing import Pool                                # Импортируем класс Pool из модуля multiprocessing

def read_info(name):                                            # Функция для чтения информации из файла.

    all_data = []                                               # Создаем локальный список для данных (не возвращается)
    with open(name, 'r') as file:                               # Открываем файл для чтения
        while True:
            line = file.readline()                              # Считываем строку из файла
            if line == '':                                      # Если строка пустая, заканчиваем считывание
                break                                           # Выходим из цикла
            all_data.append(line.strip())                       # Добавляем строку, очищая от лишних пробелов и переносов

if __name__ == '__main__':                                      # Проверка, является ли текущий модуль основным

    filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Создаем список названий файлов

    # --- Линейный вызов ---
    start_time = time.time()                                    # Запоминаем время начала выполнения
    for filename in filenames:                                  # Перебираем все файлы
        read_info(filename)                                     # Считываем информацию из каждого файла
    linear_duration = time.time() - start_time                  # Вычисляем время выполнения
    print(time.strftime("%H:%M:%S",                             # Форматируем и выводим результат
                        time.gmtime(linear_duration)) + f".{int((linear_duration % 1) * 1_000_000):06d} (линейный)")

    # --- Многопроцессный вызов ---
    start_time = time.time()                                    # Запоминаем время начала выполнения
    with Pool() as pool:                                        # Создаем пул процессов
        pool.map(read_info, filenames)                          # Выполняем считывание из всех файлов одновременно
    multi_duration = time.time() - start_time                   # Вычисляем время выполнения
    print(time.strftime("%H:%M:%S",                             # Форматируем и выводим результат
                        time.gmtime(multi_duration)) + f".{int((multi_duration % 1) * 1_000_000):06d} (многопроцессный)")
