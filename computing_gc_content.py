import collections
import numpy as np

def computing_gc_content(seq):
    coll = collections.Counter(seq)
    return (coll['G'] + coll['C']) / len(seq) * 100

def wrapper(dic):
    keys = []
    gc_values = []
    for key, value in dic.items():
        keys.append(key)
        gc_values.append(computing_gc_content(value))
    argm = np.argmax(gc_values)
    return (keys[argm], gc_values[argm])

if __name__ == '__main__':
    filename = 'computing_gc_content.txt'
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        dictionary = {}
        temp = ''
        for line in lines:
            if '>' in line:
                temp = line[1:]
                dictionary[temp] = ''
            else:
                dictionary[temp] += line
        result = wrapper(dictionary)
        print(result[0])
        print('{:.6f}'.format(result[1]))
        