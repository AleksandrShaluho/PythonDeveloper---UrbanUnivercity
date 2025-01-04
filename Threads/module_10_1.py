import time
import threading


def elapsed_time(func):
    """Decorator for measuring function execution time """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        formatted_time = time.strftime('%H:%M:%S', time.gmtime(finish_time - start_time))
        print(f'Время выполнения задачи: {formatted_time}')
        return result

    return wrapper


@elapsed_time
def writing_threads(words_numbers: tuple):
    """Writes multiple files (by the number of arguments) with typical strings using the function 'write_words'
       and threads"""
    global files_count
    threads = []
    for words_number in words_numbers:
        threads.append(threading.Thread(target=write_words, args=(words_number, f'example{files_count}.txt')))
        files_count += 1
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


@elapsed_time
def writing_funcs(words_numbers: tuple):
    """Writes multiple files (by the number of arguments) with typical strings using the function 'write_words' """
    global files_count
    for words_number in words_numbers:
        write_words(words_number, f'example{files_count}.txt')
        files_count += 1


def write_words(words_number: int, filename: str) -> None:
    """Writes a string to a file the number of times specified by the argument."""
    with open(filename, 'w', encoding='utf-8') as file:
        for number in range(1, words_number + 1):
            file.write(f'Какое-то слово № {number}\n')
            time.sleep(0.1)
    print(f'Завершена запись в файл {filename}')


files_count: int = 1
words_numbers: tuple = (10, 30, 200, 100)
writing_funcs(words_numbers)
writing_threads(words_numbers)
