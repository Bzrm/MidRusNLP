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

def POS(input_file):
    file = opener(input_file)
    a = re.findall('_\t[A-Z]+?\t', file)
    clean_list = []
    for word in a:
        word = re.sub('_\t([A-Z]+?)\t', r'\1', word)
        clean_list.append(word)
    return clean_list

#Вместо all_rd.conllu - файл, который вы прогоняете через свою обученную модель
#Вместо pred_POS_rd.txt - файл, в который запишутся все его теги частей речи
#Вместо rd_tags.txt - файл, который получился после прогона через модель
#Вместо true_POS_rd.txt - файл, в который запишутся все его теги частей речи
#Вместо labels.txt - файл, в который запишутся все возможные теги частей речи

writer(' '.join(POS('all_rd.conllu')), 'pred_POS_rd.txt')
writer(' '.join(POS('rd_tags.txt')), 'true_POS_rd.txt')
writer(' '.join(set(POS('all_rd.conllu'))), 'labels.txt')    

