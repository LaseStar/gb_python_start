# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока
# nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000]
# "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
#
#
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
# Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
import re

# встречаються ipv6 поэтому пришлось хитрить
RE_REMOTE_ADDRESS = re.compile(r'[^\s]*(?!- )[^\s]*')
# тут понятно ищем [ и до ]
RE_REQUEST_DATETIME = re.compile(r'(?<=[&\[])([^&]+)\]')
# тут опять хитрим ибо бывают типы HEAD, помимо GET
RE_REQUEST_TYPE = re.compile(r'"(\w+)')
# тут тупо через пойск " /"
RE_REQUESTED_RESOURCE = re.compile(r' (/\w+/\w+)')
# аналогично + через 2 group
RE_RESPONSE_CODE_SIZE = re.compile(r'" (\d+) (\d+)')

with open('nginx_logs.txt') as f:
    for line in f:
        remote_add = RE_REMOTE_ADDRESS.match(line).group()
        request_datetime = RE_REQUEST_DATETIME.search(line).group(1)
        request_type = RE_REQUEST_TYPE.search(line).group(1)
        requested_resource = RE_REQUESTED_RESOURCE.search(line).group(1)
        response_code = RE_RESPONSE_CODE_SIZE.search(line).group(1)
        response_size = RE_RESPONSE_CODE_SIZE.search(line).group(2)
        parsed_raw = (remote_add, request_datetime, request_type, requested_resource, response_code, response_size)
        print(parsed_raw)
