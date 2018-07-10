with open('quran.txt', 'r', encoding='utf-8') as f:
    l = f.readlines()
    quran = []
    for item in l:
        item = item.replace('۰', '')
        item = item.replace('۱', '')
        item = item.replace('۲', '')
        item = item.replace('۳', '')
        item = item.replace('۴', '')
        item = item.replace('۵', '')
        item = item.replace('۶', '')
        item = item.replace('۷', '')
        item = item.replace('۸', '')
        item = item.replace('۹', '')
        aye = item.split('()')
        for line in aye:
            quran.append(line.split('﴿﴾'))
            if quran[-1][0] == '\n':
                quran.pop()

for i in range(len(quran)):
    if len(quran[i]) < 2:
        continue
    temp = quran[i][1]
    for j in range(len(quran[i][1])):
        if quran[i][1][j] == '[':
            begin = j
        if quran[i][1][j] == ']':
            end = j
            string = quran[i][1][begin:end + 2]
            temp = temp.replace(string, '')
    quran[i][1] = temp

s = 'بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ به نام خداوند رحمتگر مهربان '
j = 0
for i in quran:
    if s in i[0]:
        i[0] = i[0].replace(s, '')

quran.pop()


def manual():
    with open('src.txt', 'w', encoding='utf-8') as f:
        for item in quran:
            f.write(item[1].strip())
            f.write('\n')

    with open('dest.txt', 'w', encoding='utf-8') as f:
        for item in quran:
            f.write(item[0].strip())
            f.write('\n')

    with open('one.txt', 'w', encoding='utf-8') as f:
        for item in quran:
            f.write(item[1].strip())
            f.write(' ||| ')
            f.write(item[0].strip())
            f.write('\n')


def openNMT():
    with open('src-train.txt', 'w', encoding='UTF-8') as f:
        for i in range(len(quran) - 1000):
            f.write(quran[i][1].strip())
            f.write('\n')

    with open('src-val.txt', 'w', encoding='UTF-8') as f:
        for i in range(len(quran) - 1000, len(quran)):
            f.write(quran[i][1].strip())
            f.write('\n')

    with open('tgt-train.txt', 'w', encoding='UTF-8') as f:
        for i in range(len(quran) - 1000):
            f.write(quran[i][0].strip())
            f.write('\n')

    with open('tgt-val.txt', 'w', encoding='UTF-8') as f:
        for i in range(len(quran) - 1000, len(quran)):
            f.write(quran[i][1].strip())
            f.write('\n')


openNMT()
