from requests import get
# from decimal import Decimal
from datetime import datetime


def currency_rates(currency_code):
    currency_code = currency_code.upper()
    # обращаемся к нашему url
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    res = get(url)
    if not res:
        print('Response Failed')
        print(res.status_code)
        return None
    # Выводим сообщение что мы подключились
    print('Response OK')

    rate_text = res.text
    # Проверяем если вообще такая валюта
    if rate_text.find(currency_code) == -1:
        print(f'Валюта {currency_code} не найдена')
        return None

    _rate = rate_text[rate_text.find(currency_code):]
    rate = (_rate[_rate.find('<Value>')+len('<Value>'):_rate.find('</Value>')])
    rate_float = float(rate.replace(',', '.'))
    # rate_decimal = Decimal(rate_float)

    # Работаепм с датой курса
    date = rate_text[rate_text.find('Date=')+len('Date='):rate_text.find('name=')-1]
    date_string = date.replace('"', '')
    date_formatter = "%d.%m.%Y"
    date = datetime.strptime(date_string, date_formatter).date()
    return print(f'Курс {currency_code} на {date} : {rate_float}')


if __name__ == '__main__':
    currency_rates('byn')
    currency_rates('usd')
