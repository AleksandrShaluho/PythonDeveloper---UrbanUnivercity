# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделкам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

# TODO написать код в однопоточном/однопроцессорном стиле


"""
Мое решение

Правильный ли подход я выбрал???

Решение построено исходя из следующего понимания задачи:
1. Заранее задана структура класса с методом run. Следовательно, ожидается в будущем создание объектов-потоков,
    выполняющих в run наиболее нагруженную и долгую задачу. Поскольку такой задачей является считывание
    данных о ценах сделок из файлов и расчет волатильности, то объектом-потоком, ВИДИМО, должен быть
    фин. инструмент. Для этих целей создан class Ticker.
2. Получение названия тикера - из названия файла. Для упрощения задачи. Хотя я понимаю по своей практике,
    что ориентироваться на названия файлов - нельзя (никаких гарантий, что оно не было исправлено ручками).
3. Обработка списка\кортежа\словаря с элементами float быстрее, чем повторное чтение файла (проверял) -
    данные однократно считываются и файл закрывается. Далее работаем уже с полученными данными. Вопрос дискуссионный _
    при наличии потоков/процессов может оказаться выгоднее читать файл несколько раз чем крутить список в памяти.
4. Для соблюдения ООП управлять расчетами (запускать потоки в следующих этапах задачи) будет class Trader -
    его задача похожа на работу трейдера-аналитика: поиск волатильных инструментов -
    часть подготовительной работы по поиску вариантов для сделок. Дискуссионная часть - запуск расчета волатильности при
    создании экземпляра класса или при вызове конкретного метода по выводу информации о волатильности.
5. Учитывая формат исходных файлов, будет использоваться стандартный модуль csv.
"""

import csv
import os
import datetime


class Ticker:
    """
    The class is designed to receive information on a specific financial instrument.
    Information is loaded from source data files.
    """

    def __init__(self, name:str,data_file: str) -> None:
        """
        The constructor for creating an object with data on a specific financial instrument
        Parameters:
            name(str): ticker of financial instrument
            data_file(str): name of file with market data for ticker
        """
        self.name = name
        self.data_file = data_file
        self.volatility: float = 0.0


    def run(self) -> float:
        """
        The method that takes data from a file for a specific ticker and calculates volatility
        """
        # Вариант с применением списковой сборки. Файл читается однократно в список и затем обрабатывается список значений
        with open(self.data_file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            prices = [float(column['PRICE']) for column in reader]
            max_price=max(prices)
            min_price = min(prices)
            average_price = (max_price+min_price)/2

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
        self.volatility = round(((max_price-min_price)/average_price)*100,2)
        return self.volatility


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
        #словарь, в который записываются пары "тикер: волатильность"
        self.volatilities={}
        # при создании экземпляра класса сразу получаем список тикеров и информацию о волатильности каждого
        for file in os.listdir(self.deals_path):
            if file.lower().endswith('.csv'):
                ticker_name = file[7:-4]
                self.tickers.append(Ticker(ticker_name, fr'{self.deals_path}\{file}'))
        for ticker in self.tickers:
            self.volatilities[ticker.name] = ticker.run()
        #все выходные параметры для задачи записываем в атрибуты экземпляра класса чтобы можно было использовать повторно без пересчета
        self.zero_volatility: list[str, ...] = []
        self.top_volatility: list[tuple[str,float], ...] =[]
        self.bottom_volatility: list[tuple[str,float], ...] =[]

    def volatility_dashboard(self):
        """
        The method displays analytical information on the volatility of instruments on the console:
        tickers with zero volatility, leaders and outsiders in volatility
        """
        #нулевая волатильность, список тикеров
        self.zero_volatility = [key for key in self.volatilities.keys() if self.volatilities[key] == 0]
        print('Нулевая волатильность:')
        print(*self.zero_volatility, sep =', ')

        # подготовка из словаря сортированного списка кортежей с исключением пар с нулевой волатильностью
        non_zero_vol = {key: value for key, value in self.volatilities.items() if value > 0}
        sorted_vol = sorted(non_zero_vol.items(), key=lambda item : item[1], reverse=True)

        # топ-3 максимальной и минимальной волатильности
        self.top_volatility = sorted_vol[:3]
        self.bottom_volatility = sorted_vol[-3:]
        print('Максимальная волатильность:')
        for x in self.top_volatility:
            print(f'{x[0]} : {x[1]}%')
        print('Минимальная волатильность:')
        for x in self.bottom_volatility:
            print(f'{x[0]} : {x[1]}%')

# запуск. Среднее время выполнения задачи - 4.06 сек
start_time = datetime.datetime.now()
tr = Trader(r'C:\Users\Александр\PycharmProjects\PythonDeveloper---UrbanUnivercity\Threads\ADD-ON\trades')
tr.volatility_dashboard()
finish_time = datetime.datetime.now()
print(f'Время выполнения задачи: {finish_time - start_time}')





