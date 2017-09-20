import reader

def match(one, two):
    if one == two:
        return 0
    return 1

dic = reader.fastaToDic('input')
s1 = dic.values()[0]
s2 = dic.values()[1]

table = [[j if i == 0 else 0 if j != 0 else i for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]


for j in range(1, len(s1) + 1):
    for i in range(1, len(s2) + 1):
        table[i][j] = min(table[i - 1][j - 1] + match(s1[j - 1], s2[i - 1]), table[i][j - 1] + 1, table[i - 1][j] + 1)

# Needleman-Wunsch_algorithm

i, j, al1, al2 = len(s2), len(s1), "", ""
while i > 0 or j > 0:
    if i > 0 and j > 0 and table[i][j] == table[i - 1][j - 1] + match(s2[i - 1], s1[j - 1]):
        al1 = s1[j - 1] + al1
        al2 = s2[i - 1] + al2
        i -= 1
        j -= 1
    elif i > 0 and table[i][j] == table[i - 1][j] + 1:
        al2 = s2[i - 1] + al2
        al1 = '-' + al1
        i -= 1
    else:
        al1 = s1[j - 1] + al1
        al2 = '-' + al2
        j -= 1

with(open('output', 'w')) as w:
    w.write(str(table[len(s2)][len(s1)]))
    w.write(al1)
    w.write(al2)
