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
* Berdichevskis et al. 2016 [http://www.dialog-21.ru/media/3384/berdičevskisaetal.pdf](http://www.dialog-21.ru/media/3384/berdičevskisaetal.pdf)
* Scherrer et al. 2018 [https://researchportal.helsinki.fi/en/publications/new-developments-in-tagging-pre-modern-orthodox-slavic-texts](https://researchportal.helsinki.fi/en/publications/new-developments-in-tagging-pre-modern-orthodox-slavic-texts)

About Middle Russian Corpus 
* Moldovan 2015
* Sichinava 2014
* Lyashevskaya et al. 2018 
* Lyashevskaya 2019 [http://www.dialog-21.ru/media/4614/lyashevskayaon-163.pdf](http://www.dialog-21.ru/media/4614/lyashevskayaon-163.pdf)  
* more on Russian historical corpora: [http://ru-eval.ru/hist/research.html](http://ru-eval.ru/hist/research.html)  

NLP papers
* Milan Straka, Jana Straková (2019), UFAL MRPipe at MRP 2019: UDPipe Goes Semantic in the Meaning Representation Parsing Shared Task [pdf](https://arxiv.org/pdf/1910.11295.pdf)  
* Milan Straka, Jana Straková, Jan Hajič (2019), Evaluating Contextualized Embeddings on 54 Languages in POS Tagging, Lemmatization and Dependency Parsing [pdf](https://arxiv.org/pdf/1908.07448.pdf)  
