import sys
from conllu import parse
import re

def opener(fname):
    f = open(fname, encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def writer(result, fname):
    f = open(fname, "w", encoding = 'utf-8')
    f.write(result)
    f.close()

pred = input('pred file: ')
true = input('true file: ')
d = input('pred POS: ')
e = input('true POS: ')

a = opener(pred)
b = opener(true)

sentences = parse(a)
sentences2 = parse(b)

result = ''
for i in range(len(sentences)):
    for j in range(len(sentences[i])):
        if sentences[i][j]['upostag'] == d:
            if sentences2[i][j]['upostag'] == e:
                result += re.sub('TokenList<(.+)>', r'\1', str(sentences[i])) + '\n'
                result += '{} {} {}\n\n'.format(sentences[i][j]['form'], sentences[i][j]['upostag'], sentences2[i][j]['upostag'])

writer(result, 'mistakes.txt')

