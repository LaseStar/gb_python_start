import sys


def read_file(line1=None, line2=None):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if not line1 and not line2:
            for line in f:
                print(line.rstrip())
        elif line1 and not line2:
            for idx, item in enumerate(f):
                if idx >= line1:
                    print(item.rstrip())
        else:
            for idx, item in enumerate(f):
                if line1 <= idx <= line2:
                    print(item.rstrip())


list_arg = sys.argv
try:
    read_file(int(list_arg[1]) - 1, int(list_arg[2]) - 1)
except IndexError:
    try:
        read_file(int(list_arg[1])-1)
    except IndexError:
        read_file()
