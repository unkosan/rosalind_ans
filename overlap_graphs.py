def load_fasta(filename: str) -> dict:
    result = {}
    with open(file=filename, mode='r') as f:
        lines = f.read().splitlines()
        temp = ''
        for line in lines:
            if line.startswith('>'):
                temp = line[1:]
                result[temp] = ''
            else:
                result[temp] += line
    return result

def overlap_graphs(adja_num: int, datadict: dict) -> list:
    keys = list(datadict.keys())
    result = []
    for previouskey in keys:
        for nextkey in keys:
            if previouskey == nextkey:
                continue
            if datadict[previouskey][-adja_num:] == datadict[nextkey][:adja_num]:
                result.append((previouskey, nextkey))
    return result

if __name__ == '__main__':
    data = load_fasta('overlap_graphs.txt')
    result = overlap_graphs(adja_num=3, datadict=data)
    for taple in result:
        print('{} {}'.format(taple[0], taple[1]))