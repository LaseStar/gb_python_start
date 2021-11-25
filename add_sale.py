import sys


sale = sys.argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.writelines(sale+'\n')
