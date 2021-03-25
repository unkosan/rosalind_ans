import collections
import numpy as np

def fasta_to_dict(filename: str) -> dict:
    result = {}
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        temp = ''
        for line in lines:
            if '>' in line:
                temp = line[1:]
                result[temp] = ''
            else:
                result[temp] += line
    return result

def profiling(data: dict) -> dict:
    result = {'A': [], 'T': [], 'G': [], 'C': []}
    for loc_taple in zip(*data.values()):
        count = collections.Counter(loc_taple)
        for nuc in result.keys():
            result[nuc].append(count[nuc])
    return result

def consensus(profiled_data: dict) -> str:
    keys, values = list(profiled_data.keys()), list(profiled_data.values())
    values = np.array(values)
    result = ''.join([keys[index] for index in np.argmax(values, axis=0)])
    return result

if __name__ == '__main__':
    filename = 'consensus_and_profile.txt'
    dictionary = fasta_to_dict(filename=filename)
    profile = profiling(data=dictionary)
    cons = consensus(profiled_data=profile)
    
    print(cons)
    for key in ['A', 'C', 'G', 'T']:
        print('{}:'.format(key) + (' {}'*len(profile[key])).format(*profile[key]))