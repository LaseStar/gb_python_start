#  (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов
#  из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

list_line = []
list_ip = []
dick_ip = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        l_split = line.split()
        list_ip.append(l_split[0])
        # Пробуем через словарь
        dick_ip.setdefault(l_split[0], 0)
        dick_ip[l_split[0]] += 1

set_ip = set(list_ip)
meeting = 0
ip = ''
for i in set_ip:
    meeting_ = list_ip.count(i)
    if meeting_ > meeting:
        meeting = meeting_
        ip = i

print('спамер ip: ', ip, 'встречается ', meeting)

# Через словарь
spam_dict = sorted(dick_ip.items(), key=lambda x: x[1], reverse=True)
print(spam_dict[:1])
