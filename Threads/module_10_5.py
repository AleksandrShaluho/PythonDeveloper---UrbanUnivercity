import datetime
import multiprocessing


def elapsed_time(func):
    """Decorator for measuring function execution time """

    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        finish_time = datetime.datetime.now()
        print(f'Время выполнения задачи: {str(finish_time - start_time)}')
        return result

    return wrapper


@elapsed_time
def read_info_multiproc(names: tuple[str, ...]) -> None:
    """
    Reads multiple files (line by line) to the list using multiprocessing. Only for test. Returns nothing
    Parameters:
        names(tuple[str,...]): name file for reading
    """
    with multiprocessing.Pool(len(names)) as p:
        p.map(read_info, names)


@elapsed_time
def read_info_func(names: tuple[str, ...]) -> None:
    """
    Reads multiple files (line by line) to the list. Only for test. Returns nothing
    Parameters:
        names(tuple[str,...]): name file for reading
    """
    for name in names:
        read_info(name)


def read_info(name: str) -> None:
    """
    Reads file (line by line) to the list. Only for test. Returns nothing
    Parameters:
        name(str): name file for reading
    """
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == "":
                break
            else:
                all_data.append(line)


if __name__ == '__main__':
    names = ('file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt')
    read_info_func(names)
    read_info_multiproc(names)
