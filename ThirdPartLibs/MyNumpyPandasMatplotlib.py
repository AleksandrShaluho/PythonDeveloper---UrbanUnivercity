"""
A training example of working with Moscow Exchange data for technical analysis and pattern trading.
Created to study the capabilities of the requests, matplotlib, numpy and pandas libraries.
Can receive data from the exchange and build a candlestick chart for a specific instrument.
In the future, a full-fledged working tool for analytical assistance in trading will be created based on this example.
"""

import requests
# необходимо для кодирования логина и пароля пользователя при передаче в запросе
import base64
import pandas
# необходимо для передачи ответа сервера в виде xml-строки в pandas для разбора
from io import StringIO
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from enum import Enum


# класс перечислений для удобства работы с разными таймфреймами
class Timeframe(Enum):
    hour_1 = 60
    minutes_5 = 5


def MOEX_auth(user: str, password: str, url: str) -> None:
    """
    Authorization on the Moscow Exchange server
    :param user: User login
    :param password: User password
    :param url: url for authorization
    :return: nothing
    """
    # приводим имя и пароль в строку, отвечающую требованиям сервера (используя перекодирование с применением base64)
    credentials = user + ':' + password
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    auth_headers = {'Authorization': f'Basic {encoded_credentials}'}
    response = requests.get(url, headers=auth_headers)


def get_candles_data(ticker: str, timeframe: Timeframe, begin_date: str, end_date: str = '') -> pandas.DataFrame:
    """
    Receives data from the exchange on prices for a specific ticker for a specified period to build a candlestick chart
    :param ticker: ticker's name (f.e. SBER)
    :param timeframe: one of typical timeframe from Timeframe class
    :param begin_date: date from which data started
    :param end_date: date to which data finished
    :return: pandas dataframe with data of ticker prices
    """
    q_param = {'from': begin_date, 'to': end_date, 'interval': timeframe}
    response = requests.get(f'https://iss.moex.com/iss/engines/stock/markets/shares/securities/{ticker}/candles',
                            params=q_param)
    ticker_candles = pandas.read_xml(StringIO(response.text), xpath=".//row")
    # встречаются пустые строки, очищаем от них нашу панда-таблицу
    ticker_candles = ticker_candles.dropna(how='all')
    # столбцы с датами надо преобразовать в формат даты и времени, это нам понадобится для графика
    ticker_candles['begin'] = pandas.to_datetime(ticker_candles['begin'])
    ticker_candles['end'] = pandas.to_datetime(ticker_candles['end'])
    return ticker_candles


def find_double_bottom(prices: list[float], window: int = 6, tolerance: float = 0.03) -> tuple[
                                                                                             bool, dict[str, float]] | \
                                                                                         tuple[bool, None]:
    """
    Defines a "double bottom" figure in a price array.
    :param prices: list of prices
    :param window: window size for searching local extremes
    :param tolerance: permissible deviation between minimums (in fractions)
    :return: True/False and figure parameters upon detection
    """
    # Находим локальные минимумы и максимумы
    minima = []
    maxima = []

    for i in range(window, len(prices) - window):
        if is_local_min(prices, i, window):
            minima.append(i)
        elif is_local_max(prices, i, window):
            maxima.append(i)

    # Поиск подходящих пар минимумов
    for i in range(len(minima)):
        for j in range(i + 1, len(minima)):
            bottom1 = minima[i]
            bottom2 = minima[j]

            # Проверяем уровень цен
            price_diff = abs(prices[bottom1] - prices[bottom2]) / prices[bottom1]
            if price_diff > tolerance:
                continue

            # Ищем пик между ними
            peak = next((p for p in maxima if bottom1 < p < bottom2), None)
            if not peak:
                continue

            return True, {
                'first_bottom': bottom1,
                'second_bottom': bottom2,
                'peak': peak,
            }

    return False, None


def is_local_min(prices, index, window):
    return prices[index] == min(prices[index - window:index + window + 1])


def is_local_max(prices, index, window):
    return prices[index] == max(prices[index - window:index + window + 1])


def calculate_sma(data, periods=200):
    """Вычисление скользящей средней с использованием numpy"""
    weights = np.repeat(1.0, periods) / periods
    sma = np.convolve(data, weights, 'valid')
    # Добавляем NaN в начало для совпадения размеров
    return np.concatenate(([np.nan] * (periods - 1), sma))
    # return np.insert(sma, 0, [np.nan] * (periods - 1))


def get_chart(prices: pandas.DataFrame, ticker: str, sma_period=200) -> None:
    """
    Builds a candlestick chart based on the data received for a specific instrument and displays it on the screen
    """
    # Убедимся, что данные отсортированы по времени
    prices = prices.sort_values('begin').reset_index(drop=True)

    # Создаем числовой индекс для оси X (чтобы избежать проблем с пропусками времени)
    x = np.arange(len(prices))

    # Рассчитываем SMA
    sma = calculate_sma(prices.close.values, sma_period)

    # Настройки графика
    fig, ax = plt.subplots(figsize=(16, 8))

    # Параметры свечей
    candle_width = 0.8  # Фиксированная ширина свечи
    wick_width = 0.3  # Ширина теней

    # Рисуем свечи
    for i in range(len(prices)):
        row = prices.iloc[i]
        color = '#2ecc71' if row.close >= row.open else '#e74c3c'

        # Тело свечи
        ax.bar(x[i],
               height=abs(row.close - row.open),
               width=candle_width,
               bottom=min(row.open, row.close),
               color=color,
               edgecolor='black')

        # Тени
        ax.plot([x[i], x[i]],
                [row.low, row.high],
                color=color,
                linewidth=1,
                solid_capstyle='round')

    # Добавляем SMA
    ax.plot(x, sma, color='black', linewidth=2, label=f'SMA {sma_period}', zorder=3)

    # Настройка оси X
    ax.set_xticks(x[::len(prices) // 10])  # Показываем каждую 10-ю метку
    ax.set_xticklabels([d.strftime('%Y-%m-%d\n%H:%M')
                        for d in prices['begin'].iloc[::len(prices) // 10]],
                       rotation=45,
                       ha='right')

    # Поиск и отрисовка паттерна
    has_double_bottom, pattern = find_double_bottom(prices.close.values)

    if has_double_bottom:
        # Стили для элементов паттерна
        bottom_style = {'s': 120, 'marker': 'o', 'color': 'blue', 'zorder': 5}
        peak_style = {'s': 100, 'marker': 'v', 'color': 'gold', 'zorder': 5}
        line_style = {'color': 'purple', 'linestyle': '--', 'linewidth': 2}

        # Индексы паттерна
        idx1 = pattern['first_bottom']
        idx2 = pattern['second_bottom']
        peak_idx = pattern['peak']

        # Отрисовка элементов
        ax.scatter(x[idx1], prices.close.iloc[idx1], **bottom_style)
        ax.scatter(x[idx2], prices.close.iloc[idx2], **bottom_style)
        ax.scatter(x[peak_idx], prices.close.iloc[peak_idx], **peak_style)

        # Соединяющие линии
        ax.plot([x[idx1], x[peak_idx], x[idx2]],
                [prices.close.iloc[idx1],
                 prices.close.iloc[peak_idx],
                 prices.close.iloc[idx2]],
                **line_style)

    # Настройки графика
    ax.set_title(f'График {ticker}', fontsize=16, pad=20)
    ax.set_xlabel('Время', fontsize=12)
    ax.set_ylabel('Цена', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()


def main():
    # в чем смысл авторизации так до конца и не понял, получив куки дальше его использовать негде, сервер любые запросы принимает и без куки
    # но без авторизации принимать запросы не будет. Не улавливаю механизм работы пока...
    # зарегистрироваться на бирже проще простого, это бесплатно, я не использовал платный доступ
    MOEX_auth(user='your login', password='your password', url='https://passport.moex.com/authenticate')
    # получили цены по Сберу для часового таймфрейма с 20 января
    ticker_candles = get_candles_data('AFKS', Timeframe.hour_1, '2025-01-20')
    get_chart(ticker_candles, 'AFKS', sma_period=50)


# пример исполнения программы
if __name__ == '__main__':
    try:
        main()
    except:
        print('Что-то пошло не так. Простите меня, ведь я не волшебник. Я еще только учусь')
