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

def feat_extra(pred_file, true_file):
    pred_feats = ''
    true_feats = ''
    pred = parse(opener(pred_file))
    true = parse(opener(true_file))
    for i in range(len(pred)):
        for j in range(len(pred[i])):
            if pred[i][j]['upostag'] == 'VERB':
                if true[i][j]['upostag'] == 'VERB':
                    if pred[i][j]['feats']:
                        if true[i][j]['feats']:
                            if 'Number' in pred[i][j]['feats']:
                                pred_feats += '{} '.format(pred[i][j]['feats']['Number'])
                            else:
                                pred_feats += '{} '.format('None')
                            if 'Number' in true[i][j]['feats']:
                                true_feats += '{} '.format(true[i][j]['feats']['Number'])
                            else:
                                true_feats += '{} '.format('None')                   
    return pred_feats, true_feats

pr, tr = feat_extra('all_acts.conllu', 'acts_tags.txt')

writer(pr, 'pred_number.txt')
writer(tr, 'true_number.txt')
