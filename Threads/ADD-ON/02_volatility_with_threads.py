# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

# TODO тут ваш код в многопоточном стиле


import csv
import os
import threading
import datetime


class Ticker(threading.Thread):
    """
    The class is designed to receive information on a specific financial instrument.
    Information is loaded from source data files. Using threads.
    """

    def __init__(self, name: str, data_file: str) -> None:
        """
        The constructor for creating an object with data on a specific financial instrument
        Parameters:
            name(str): ticker of financial instrument
            data_file(str): name of file with market data for ticker
        """
        threading.Thread.__init__(self)
        self.name = name
        self.data_file = data_file
        self.volatility: float = 0.0

    def run(self):
        """
        The method that takes data from a file for a specific ticker and calculates volatility
        """
        # Вариант с применением списковой сборки. Файл читается однократно в список и затем обрабатывается список значений
        with open(self.data_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            prices = [float(column['PRICE']) for column in reader]
            max_price = max(prices)
            min_price = min(prices)
            average_price = (max_price + min_price) / 2

            '''
            вариант с повторным чтением файла с помощью генераторной сборки.
            На примере TICKER_SiH9.csv показал в 2 раза худшее время по сравнению с вариантом однократного чтения файла
            с помощью списковой сборки (2.40сек против 1.25 сек)        
            with open(self.data_file, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                max_price = max(float(column['PRICE']) for column in reader)
                csv_file.seek(0)
                next(reader)
                min_price = min(float(column['PRICE']) for column in reader)
                average_price = (max_price + min_price) / 2
            '''
        self.volatility = round(((max_price - min_price) / average_price) * 100, 2)

    # результат вычисления волатильности вернем в основной поток немного модифицированным методом join
    # это позволит обойтись без использования очереди. Насколько такой подход допустим???
    '''def join(self, timeout=None):
        threading.Thread.join(self)
        return self.volatility
'''

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'Тикер: {self.name}, данные: {self.data_file}'


class Trader:
    """
    This class is designed to provide the trader with generalized information on financial instruments.
    Instances of the class receive information from objects of the Ticker type
    """

    def __init__(self, deals_path: str) -> None:
        """
        The constructor for creating an object with data on a specific financial instrument
        Parameters:
            deals_path(str): the path, where the files with data on transactions with financial instruments are located
        """
        self.deals_path = deals_path
        self.tickers: list = []

        '''
        список или словарь?
        пара "тикер: волатильность" как бы говорит об использовании словаря, но
        по условиям задачи эти данные используются ТОЛЬКО для формирования СОРТИРОВАННОГО списка лидеров и аутсайдеров
        поиска отдельных значений по ключу не предполагается, при этом нормальных (прямых) инструментов для сортировки
        и отбора значений в словаре я не нашел, все найденные методы предполагают промежуточный вариант из списка пар
        "(тикер, волатильность)" с последующим преобразование обратно в словарь. 
        я оставил исходный набор всех волатильностей в словаре, подразумевая, что функциональность класса Trader может быть
        расширена и тогда словарь пригодится. Но исходя только из условий задачи оптимальнее было бы наверное работать со списком
        кортежей
        '''
        # словарь, в который записываются пары "тикер: волатильность"
        self.volatilities = {}
        # при создании экземпляра класса сразу получаем список тикеров и информацию о волатильности каждого
        for file in os.listdir(self.deals_path):
            if file.lower().endswith('.csv'):
                ticker_name = file[7:-4]
                self.tickers.append(Ticker(ticker_name, fr'{self.deals_path}\{file}'))
        # расчеты запускаем в потоке
        for ticker in self.tickers:
            ticker.start()
        for ticker in self.tickers:
            ticker.join()

        for ticker in self.tickers:
            self.volatilities[ticker.name] = ticker.volatility

        # все выходные параметры для задачи записываем в атрибуты экземпляра класса чтобы можно было использовать повторно без пересчета
        self.zero_volatility: list[str, ...] = []
        self.top_volatility: list[tuple[str, float], ...] = []
        self.bottom_volatility: list[tuple[str, float], ...] = []

    def volatility_dashboard(self):
        """
        The method displays analytical information on the volatility of instruments on the console:
        tickers with zero volatility, leaders and outsiders in volatility
        """
        # нулевая волатильность, список тикеров
        self.zero_volatility = [key for key in self.volatilities.keys() if self.volatilities[key] == 0]
        print('Нулевая волатильность:')
        print(*self.zero_volatility, sep=', ')

        # подготовка из словаря сортированного списка кортежей с исключением пар с нулевой волатильностью
        non_zero_vol = {key: value for key, value in self.volatilities.items() if value > 0}
        sorted_vol = sorted(non_zero_vol.items(), key=lambda item: item[1], reverse=True)

        # топ-3 максимальной и минимальной волатильности
        self.top_volatility = sorted_vol[:3]
        self.bottom_volatility = sorted_vol[-3:]
        print('Максимальная волатильность:')
        for x in self.top_volatility:
            print(f'{x[0]} : {x[1]}%')
        print('Минимальная волатильность:')
        for x in self.bottom_volatility:
            print(f'{x[0]} : {x[1]}%')


# запуск. Среднее время выполнения задачи - 4.18 сек Почему время выполнения задачи стало больше чем в одном потоке???
# потоки запускаются и работают одновременно, соответственно время получения словаря волатильности должно быть меньше
# остальной код такой же. Вариант с применением очереди тоже не дал существенного ускорения.
# ????????
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    tr = Trader(r'C:\Users\Александр\PycharmProjects\PythonDeveloper---UrbanUnivercity\Threads\ADD-ON\trades')
    tr.volatility_dashboard()
    finish_time = datetime.datetime.now()
    print(f'Время выполнения задачи: {finish_time - start_time}')
