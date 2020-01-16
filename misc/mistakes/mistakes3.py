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


d = 'SYM'
e = 'PROPN'

sentences = parse(opener('all_rd.conllu'))
sentences2 = parse(opener('rd_tags.txt'))

result = ''
for i in range(len(sentences)):
    for j in range(len(sentences[i])):
        if sentences[i][j]['upostag'] == d:
            if sentences2[i][j]['upostag'] == e:
                #sents = [sent for sent in sentences[i]]
                #sents[j] = re.sub('(.+)', r'\(\1\)', sents[j])
                word = sentences[i][j]['form']
                sentences[i][j]['form'] = re.sub('(.+)', r'$\1$', sentences[i][j]['form'])
                g = re.sub(' ([\.,])', r'\1', re.sub(', ', ' ', re.sub('TokenList<(.+)>', r'\1', str(sentences[i]))))
                result += g + '\n'
                result += '{}    pred_tag: {}  true_tag: {}\n\n'.format(word, sentences[i][j]['upostag'], sentences2[i][j]['upostag'])

writer(result, 'mistakes.txt')

