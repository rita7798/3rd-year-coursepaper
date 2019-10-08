import re, os
import gensim
from gensim import corpora, models
import nltk
from nltk import FreqDist
from nltk.collocations import *
from pymystem3 import Mystem
from stop_words import get_stop_words
ru_stop = get_stop_words('ru')


mystem_object = Mystem()
mystem_object.start()


puncts = "[«–»—!\$%&'()*+,./:;<=>?@^_`{|}~']*-–—...]"
extra_words = ["понимать", "знать", "хотеть", "глаз", "рука", "голова", "увидеть", "что-то", "смотреть", "нога", "свой", 'видеть',
              'становиться', 'остаться', 'давать', 'стоять', 'оставаться', 'оказываться', 'думать']


#Fantasy
def processFile(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        print(file)
        text = f.read()[:10000000]
        print(len(text))
        words = text.split()
        for word in words:
            word = word.lower().strip("[“«–»—!\$%&'()*+,./:;<=>?@^_`{|}~'*-–—...]")
            if word != '' and word not in ru_stop:
                word = mystem_object.analyze(word)
                if word[0].get('analysis') != []:
                    try:
                        if word[0]['analysis'][0]['lex'] not in extra_words and word[0]['analysis'][0]['lex'] not in ru_stop:
                            doc.append(word[0]['analysis'][0]['lex'])
                    except:
                        continue                    
    return doc


def processDir(dir):
    doc_set = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Fantasy'):
            doc_set.append(processFile(file))
    return doc_set

        
def topic_modeling(doc_set):
    print(len(doc_set))
    dictionary = corpora.Dictionary(doc_set)
    corpus = [dictionary.doc2bow(text) for text in doc_set]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=6, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=6, num_words=10):
        for i in a:
            print (i)


doc_set = processDir('.')    
topic_modeling(doc_set)


#Adventures
def processFile(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        print(file)
        text = f.read()[:10000000]
        print(len(text))
        words = text.split()
        for word in words:
            word = word.lower().strip("[“«–»—!\$%&'()*+,./:;<=>?@^_`{|}~'*-–—...]")
            if word != '' and word not in ru_stop:
                word = mystem_object.analyze(word)
                if word[0].get('analysis') != []:
                    try:
                        if word[0]['analysis'][0]['lex'] not in extra_words and word[0]['analysis'][0]['lex'] not in ru_stop:
                            doc.append(word[0]['analysis'][0]['lex'])
                    except:
                        continue                    
    return doc


def processDir(dir):
    doc_set = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Adventures'):
            doc_set.append(processFile(file))
    return doc_set

        
def topic_modeling(doc_set):
    print(len(doc_set))
    dictionary = corpora.Dictionary(doc_set)
    corpus = [dictionary.doc2bow(text) for text in doc_set]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=6, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=6, num_words=10):
        for i in a:
            print (i)


doc_set = processDir('.')    
topic_modeling(doc_set)


#Scifi
def processFile(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        print(file)
        text = f.read()[:10000000]
        print(len(text))
        words = text.split()
        for word in words:
            word = word.lower().strip("[“«–»—!\$%&'()*+,./:;<=>?@^_`{|}~'*-–—...]")
            if word != '' and word not in ru_stop:
                word = mystem_object.analyze(word)
                if word[0].get('analysis') != []:
                    try:
                        if word[0]['analysis'][0]['lex'] not in extra_words and word[0]['analysis'][0]['lex'] not in ru_stop:
                            doc.append(word[0]['analysis'][0]['lex'])
                    except:
                        continue                    
    return doc


def processDir(dir):
    doc_set = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Scifi'):
            doc_set.append(processFile(file))
    return doc_set

        
def topic_modeling(doc_set):
    print(len(doc_set))
    dictionary = corpora.Dictionary(doc_set)
    corpus = [dictionary.doc2bow(text) for text in doc_set]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=6, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=6, num_words=10):
        for i in a:
            print (i)


doc_set = processDir('.')    
topic_modeling(doc_set)


#Horror
def processFile(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        print(file)
        text = f.read()[:10000000]
        print(len(text))
        words = text.split()
        for word in words:
            word = word.lower().strip("[“«–»—!\$%&'()*+,./:;<=>?@^_`{|}~'*-–—...]")
            if word != '' and word not in ru_stop:
                word = mystem_object.analyze(word)
                if word[0].get('analysis') != []:
                    try:
                        if word[0]['analysis'][0]['lex'] not in extra_words and word[0]['analysis'][0]['lex'] not in ru_stop:
                            doc.append(word[0]['analysis'][0]['lex'])
                    except:
                        continue                    
    return doc


def processDir(dir):
    doc_set = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Horror'):
            doc_set.append(processFile(file))
    return doc_set

        
def topic_modeling(doc_set):
    print(len(doc_set))
    dictionary = corpora.Dictionary(doc_set)
    corpus = [dictionary.doc2bow(text) for text in doc_set]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=6, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=6, num_words=10):
        for i in a:
            print (i)


doc_set = processDir('.')    
topic_modeling(doc_set)


#Detectives
def processFile(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        print(file)
        text = f.read()[:10000000]
        print(len(text))
        words = text.split()
        for word in words:
            word = word.lower().strip("[“«–»—!\$%&'()*+,./:;<=>?@^_`{|}~'*-–—...]")
            if word != '' and word not in ru_stop:
                word = mystem_object.analyze(word)
                if word[0].get('analysis') != []:
                    try:
                        if word[0]['analysis'][0]['lex'] not in extra_words and word[0]['analysis'][0]['lex'] not in ru_stop:
                            doc.append(word[0]['analysis'][0]['lex'])
                    except:
                        continue                    
    return doc


def processDir(dir):
    doc_set = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Detectives'):
            doc_set.append(processFile(file))
    return doc_set

        
def topic_modeling(doc_set):
    print(len(doc_set))
    dictionary = corpora.Dictionary(doc_set)
    corpus = [dictionary.doc2bow(text) for text in doc_set]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=6, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=6, num_words=10):
        for i in a:
            print (i)


doc_set = processDir('.')    
topic_modeling(doc_set)


#Cyber
def processFile(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        print(file)
        text = f.read()
        print(len(text))
        words = text.split()
        for word in words:
            word = word.lower().strip("[“«–»—!\$%&'()*+,./:;<=>?@^_`{|}~'*-–—...]")
            if word != '' and word not in ru_stop:
                word = mystem_object.analyze(word)
                if word[0].get('analysis') != []:
                    try:
                        if word[0]['analysis'][0]['lex'] not in extra_words and word[0]['analysis'][0]['lex'] not in ru_stop:
                            doc.append(word[0]['analysis'][0]['lex'])
                    except:
                        continue                    
    return doc


def processDir(dir):
    doc_set = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Cyber'):
            doc_set.append(processFile(file))
    return doc_set

        
def topic_modeling(doc_set):
    print(len(doc_set))
    dictionary = corpora.Dictionary(doc_set)
    corpus = [dictionary.doc2bow(text) for text in doc_set]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=6, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=6, num_words=10):
        for i in a:
            print (i)


doc_set = processDir('.')    
topic_modeling(doc_set)