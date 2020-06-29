from conllu import parse

def opener(fname):
    f = open(fname, encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def writer(result, fname):
    f = open(fname, "w", encoding = 'utf-8')
    f.write(result)
    f.close()

def uniq_set(file):
    words = []
    text = parse(opener(file))
    for i in text:
        for j in i:
            words.append(j['form'])
    uniq_words = set(words)
    return uniq_words

def jaccard(uniq_train, uniq_test):
    all_words = uniq_train.union(uniq_test)
    intr = uniq_train.intersection(uniq_test)
    jaccard_coef = len(intr)/len(all_words)
    return jaccard_coef


train_files = [filenames] # сюда записывать пути к трейнам
test_file_1 = filename # а сюда путь к тесту
uniq_words_test_1 = uniq_set(test_file_1)
#test_file_2 = 'TEST_2.txt' # здесь можно вставить ещё один тест
#uniq_words_test_2 = uniq_set(test_file_2)
for file in train_files:
    #file_name = str(file)
    uniq_words_train = uniq_set(file)
    #uniq_words_test_1 = uniq_set(test_file_1)
    #uniq_words_test_2 = uniq_set(test_file_2)
    result_test_1 = jaccard(uniq_words_train, uniq_words_test_1)
    print(result_test_1)
    #result_test_2 = jaccard(uniq_words_train, uniq_words_test_2)
    #result_text = ('Результат для ', file, ' на ', test_file_1, ' - ' , result_test_1)#, '\n', 'Результат для ', file,
                   #' на ', test_file_2, ' - ' , result_test_2, '\n', '\n')
    #with open('results_jac_50.txt', "a", encoding='utf-8') as f:
        #f.write(str(result_text))




#uniq_words_train = uniq_set('Kusok_5.txt')
#uniq_words_test = uniq_set('TEST.txt')
#result = jaccard(uniq_words_train, uniq_words_test)
#print(result)
#print(len(uniq_words_train))
#print(len(uniq_words_test))
#all_words = uniq_words_train.union(uniq_words_test)
#intr = uniq_words_train.intersection(uniq_words_test)
#print(len(all_words))
#print(len(intr))

#print(uniq_words_train)