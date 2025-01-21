"""
The module is designed to check whether counterparties (legal entities and entrepreneurs) use electronic document management.
For this, the following are used:
1) list of counterparties' TINs
2) data from the "Transparent Business" website (pb.nalog.ru)
3) requests and json libraries

A POST request is sent to the website server (the address and request parameters are obtained by using the developer's tools
in the browser to analyze outgoing requests from the website to the server).
The algorithm works in 2 stages in accordance with the order in which the server processes the request:
Stage 1: sending a request with the TIN to the server and receiving a response from it that the request has been accepted
         and the response is ready, with the response ID.
Stage 2: sending a request with the response ID to receive information.

Considering that the request is made by a unique identifier - TIN, the probability of receiving a list
of several companies in response was not considered and parsing is not provided.

The output result is the output to the console of information on each counterparty: TIN, name, whether or not it uses
electronic document management.
"""

import requests
import json
from time import sleep

# в конечном итоге получаем от сервера словарь с несколькими уровнями вложений, которые могут также быть словарями и списками
# нам нужны 3 конкретных элемента. У нас стандартная структура ответа сервера в данном случае и ключи также заранее известны
# поэтому потребности в рекурсивном обходе нет

def is_using_EDO(TINs:list[str], url:str)->None:
    """
    the function sends a request containing the TIN to the site specified in the parameters, parses the response received
    in the l;zhi format and, based on the response, determines whether the counterparty uses electronic document management
    :param TINs: list of TINs (str)
    :param url: string with URL of site "Transparent business"
    :return: noting
    """
    for TIN in TINs:
        # 1 этап обращения к серверу. Отправляем ему ИНН и получаем id ответа
        INN_query_string={'mode':'search-all','queryAll':TIN}
        INN_parsed_response = json.loads(requests.post(url,data=INN_query_string).text)

        # 2 этап обращения к серверу. Отправляем ему id ответа и служебную строку о том, что хотим получить содержание ответа
        id_query_string = {'id':INN_parsed_response['id'],"method":"get-response"}
        id_parsed_response = json.loads(requests.post(url,data=id_query_string).text)
        # ответ распарсили в словарь и теперь ищем значения нужных нам ключей и выводим в консоль
        #к сожалению сервер не дает отдельного признака типа контрагента (юр.лицо или предприниматель), поэтому ориентируемся на наличие содержимого
        #соответствующих блоков в ответе
        company_type = 'ul'
        EDO_info = {
            '1': "Применяет ЭДО",
            '2': "Не применяет ЭДО"
        }
        if not id_parsed_response[company_type]['data']:
            company_type = 'ip'
        company_name = id_parsed_response[company_type]['data'][0]['namec']
        is_EDO = EDO_info[id_parsed_response[company_type]['data'][0]['predo']]
        print(f'ИНН: {TIN},  Наименование: {company_name},  Участник ЭДО: {is_EDO}')
        #сервер очень не любит когда его мучают вопросами. Чтобы он не требовал ввести цифры с картинками
        #ставим таймаут между итерациями. К сожалению, сервер не хочет видеть нас чаще, чем каждые 2 минуты
        sleep(120)

def main():
    url = 'https://pb.nalog.ru/search-proc.json'
    INNs = ['7725114488', '3328409738', '143511687362', '7721583168', '7721524282', '772265085092', '9731025141',
        '614103495002']
    is_using_EDO(INNs, url)

main()