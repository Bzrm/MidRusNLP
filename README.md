# MidRusNLP

Middle Russian natural language processing


### Useful links  

* [UD project](https://universaldependencies.org)  
* [UD github](https://github.com/)  
* [Validation scripts](https://github.com/UniversalDependencies/tools/blob/master/README.txt)  
  * cat \*.conllu | python validate.py --lang orv --max-err=0
* [RNC Middle Russian in UD](https://github.com/UniversalDependencies/UD_Old_Russian-RNC/tree/dev) NB use dev branch   
* [TOROT in UD](https://github.com/UniversalDependencies/UD_Old_Russian-TOROT/tree/dev) NB use dev branch  
* [RNC online](http://ruscorpora.ru/new/search-mid_rus.html)  

### Corpus annotation  
* [Morphology](https://github.com/olesar/UD_MidRussian)  

### Search and browse  
* [Arborator](https://arborator.ilpga.fr/q.cgi)  
* [UDpipe viewer](http://lindat.mff.cuni.cz/services/udpipe/)  

### NLP tools  
* [UDpipe]()   
  * UDpipe API `curl -F data=@temp.conllu -F model=russian-gsd-ud-2.5-191206 -F tagger= -F parser= http://lindat.mff.cuni.cz/services/udpipe/api/process | PYTHONIOENCODING=utf-8 python -c "import sys,json; sys.stdout.write(json.load(sys.stdin)['result'])" > temp.conllu` see [more](http://lindat.mff.cuni.cz/services/udpipe/api-reference.php)  
  * training UDpipe: Apertium [tutorial](http://wiki.apertium.org/wiki/UDPipe)  
  * UDpipe models: [list](http://lindat.mff.cuni.cz/services/udpipe/api/models)

### References  
About the Middle Russian Corpus 
* Moldovan 2015
* Sichinava 2014: Сичинава Д.В. Исторические корпуса Национального корпуса русского языка как инструмент диахронических исследований грамматики / Д.В.Сичинава // Писменото наследство и информационните технологии. El'Manuscript–2014. Материали от V международна научной конференции / В.А.Баранов, В. Желязкова, А.М.Лаврентьев, отв. ред. – София, Ижевск, 2014.
* Lyashevskaya 2018 [gold data](https://libweb.kpfu.ru/publication/papers/kls/2018-1/KLS-2018-1-131-135.pdf)
* Lyashevskaya 2019 [http://www.dialog-21.ru/media/4614/lyashevskayaon-163.pdf](http://www.dialog-21.ru/media/4614/lyashevskayaon-163.pdf)  
* more on Russian historical corpora: [http://ru-eval.ru/hist/research.html](http://ru-eval.ru/hist/research.html)  

NLP papers
* Milan Straka, Jana Straková (2019), UFAL MRPipe at MRP 2019: UDPipe Goes Semantic in the Meaning Representation Parsing Shared Task [pdf](https://arxiv.org/pdf/1910.11295.pdf)  
* Milan Straka, Jana Straková, Jan Hajič (2019), Evaluating Contextualized Embeddings on 54 Languages in POS Tagging, Lemmatization and Dependency Parsing [pdf](https://arxiv.org/pdf/1908.07448.pdf)  
* Scherrer Y. et al. (2018). New developments in tagging pre-modern Orthodox Slavic varieties / Y.Scherrer, S.Mocken, A.Rabus // Scripta & e-Scripta, 2018. – Т.18. [https://researchportal.helsinki.fi/en/publications/new-developments-in-tagging-pre-modern-orthodox-slavic-texts](https://researchportal.helsinki.fi/en/publications/new-developments-in-tagging-pre-modern-orthodox-slavic-texts)
* Berdičevskis A. et al. 2016. The beginning of a beautiful friendship: rule-based and statistical analysis of Middle Russian / А.Berdičevskis, H.M.Eckhoff., T.Gavrilova // Компьютерная лингвистика и интеллектуальные технологии. Труды международной конференции «Диалог». – М., 2016. – С. 99–111. [http://www.dialog-21.ru/media/3384/berdičevskisaetal.pdf](http://www.dialog-21.ru/media/3384/berdičevskisaetal.pdf)  
* Архангельский Т.А. и др. 2014. Система электронной грамматической разметки древнерусских и церковнославянских текстов и её использование в веб-ресурсах / Т.А.Архангельский, Е.А.Мишина, А.А.Пичхадзе // Писменото наследство и информационните технологии. El'Manuscript–2014. Материали от V международна научной конференции / В.А.Баранов, В.Желязкова, А.М.Лаврентьев. – София, Ижевск, 2014. [pdf](http://textualheritage.org/index.php?option=com_docman&task=doc_download&gid=392&Itemid=&lang=ru)  
* Баранов В.А. 2007. Автоматический морфологический анализатор древнерусского языка: лингвистичекие и технологические решения / В.А.Баранов, А.Н.Миронов, А.Н.Лапин и др. // 10-я юбилейная междунар. конф. «EVA 2007 Москва». – М., 2007. [pdf](http://conf.evarussia.ru/upload/eva2007/reports/doklad_1318.pdf)  
* Гаврилова Т.С. и др. 2016. К задаче автоматической лексико-грамматической разметки старорусского корпуса XV–XVII вв. / Т.С.Гаврилова, Т.А.Шалганова, О.Н.Ляшевская // Вестник ПСТГУ. Серия «Филология». 2016. – Т.47. – Вып. 2. – С. 7–25. [pdf](https://cyberleninka.ru/article/n/k-zadache-avtomaticheskoy-leksiko-grammaticheskoy-razmetki-starorusskogo-korpusa-xv-xvii-vv)  
* Гаврилова Т.С., Шалганова Т.А., Ляшевская, О.Н. 2017. _Взiaлъ_, _възялъ_, _вьзял_: обработка орфографической вариативности при лексико-грамматической аннотации старорусского корпуса XV-XVII вв. Вестник Православного Свято-Тихоновского гуманитарного университета. Серия 3: Филология, (51). [pdf](http://periodical.pstgu.ru/pdf/files/article/ru/1498120157.1_Gavrilova_i_dr_11-20.pdf)  
* Meyer R. New wine in old wineskins? Tagging Old Russian via annotation projection from modern translations / R.Meyer // Russian linguistics, 2011. – Т. 35. – No 2. – P.267–281. [pdf](https://www.researchgate.net/publication/261977705_New_wine_in_old_wineskins-Tagging_Old_Russian_via_annotation_projection_from_modern_translations_Molodoe_vino_v_mehi_vethie-Razmetka_drevnerusskih_tekstov_posredstvom_proekcii_annotacii_iz_sovremennyh)   
* Segalovich I. A Fast Morphological Algorithm with Unknown Word Guessing Induced by a Dictionary for a Web Search Engine / I.Segalovich // Proceedings of MLMTA, Las Vegas, Nevada, 2003. – P. 273–280. [pdf](https://www.semanticscholar.org/paper/A-Fast-Morphological-Algorithm-with-Unknown-Word-by-Segalovich/983b7014df3b7d4e82e32ba4f45f71f3879f8c96)  
* Zeman D. CoNLL 2018 Shared Task: Multilingual Parsing from Raw Text to Universal Dependencies / D.Zeman, J.Hajič, M.Popel, M.Potthast, M.Straka, F.Ginter, J.Nivre, S.Petrov // Proceedings of the CoNLL 2018 Shared Task.– Brussels, 2018. – P. 1–21.
