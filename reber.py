#script to implement the reber grammar shown in homl.info/108
#to train an RNN

import random

reber_values = [
        ['', 'b', '', '', '', '', '', ''],
        ['', '', 't', '', 'p', '', '', ''],
        ['', '', 's', 'x', '', '', '', ''],
        ['', '', '', '', 'x', '', 's', ''],
        ['', '', '', '', 't', 'v', '', ''],
        ['', '', '', 'p', '', '', 'v', ''],
        ['', '', '', '', '', '', '', 'e'],
        ['', '', '', '', '', '', '', ''],
    ]

reber_matrix = {}

for i in range(len(reber_values)):
    reber_matrix[i] = [j for j in range(len(reber_values[0])) if reber_values[i][j] != '']

print(reber_matrix)

def generate_reber():
    reb_str = ''
    to_add = reber_values[0][1]
    i = 1

    while i != 7:
        reb_str += to_add
        j = i
        i = random.choice(reber_matrix[i])
        to_add = reber_values[j][i]

    return reb_str + 'e'

def check_reber(s):
    if s[0] != 'b' or s[-1] != 'e':
        return False

    cur_val = 'b'
    k = 0
    i = 1

    while cur_val != 'e' and k < len(s) - 1:
        #print(f'print checking {s[k]}')
        #print(f'k = {k}, i = {i}')
        if s[k+1] not in reber_values[i]:
            return False

        else:
            i = reber_values[i].index(s[k+1])
            k += 1;

    return True
