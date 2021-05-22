import matplotlib.pyplot as plt
import math



def read_all_lines(filename):
    f = open(filename)
    res = f.readlines()
    f.close()
    return res


def convert_to_dict(lst):
    dct = []
    lst = list(map(lambda string: string.split(","), lst))
    list(map(lambda x: dct.append(dict(zip([lst[0][0], lst[0][1], lst[0][2], lst[0][3]], x))), lst))
    dct.pop(0)
    return dct


#if __name__ == '__main__':
    #a = read_all_lines('file')
    #b = convert_to_dict(a)
    #print(b)
