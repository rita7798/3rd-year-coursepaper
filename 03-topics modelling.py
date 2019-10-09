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
def processFileFantasy(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        #print(file)
        text = f.read()
        #print(len(text))
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


def processDirFantasy(dir):
    doc_setFantasy = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Fantasy'):
            doc_setFantasy.append(processFileFantasy(file))
    return doc_setFantasy

        
def topic_modelingFantasy(doc_setFantasy):
    #print(len(doc_setFantasy))
    dictionary = corpora.Dictionary(doc_setFantasy)
    corpus = [dictionary.doc2bow(text) for text in doc_setFantasy]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=4, num_words=5):
        for i in a:
            print (i)


doc_setFantasy = processDirFantasy('.')    
topic_modelingFantasy(doc_setFantasy)


#Adventures
def processFileAdventures(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        #print(file)
        text = f.read()
        #print(len(text))
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


def processDirAdventures(dir):
    doc_setAdventures = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Adventures'):
            doc_setAdventures.append(processFileAdventures(file))
    return doc_setAdventures

        
def topic_modelingAdventures(doc_setAdventures):
    #print(len(doc_setAdventures))
    dictionary = corpora.Dictionary(doc_setAdventures)
    corpus = [dictionary.doc2bow(text) for text in doc_setAdventures]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=4, num_words=5):
        for i in a:
            print (i)


doc_setAdventures = processDirAdventures('.')    
topic_modelingAdventures(doc_setAdventures)


#Scifi
def processFileScifi(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        #print(file)
        text = f.read()
        #print(len(text))
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


def processDirScifi(dir):
    doc_setScifi = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Scifi'):
            doc_setScifi.append(processFileScifi(file))
    return doc_setScifi

        
def topic_modelingScifi(doc_setScifi):
    #print(len(doc_setScifi))
    dictionary = corpora.Dictionary(doc_setScifi)
    corpus = [dictionary.doc2bow(text) for text in doc_setScifi]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=4, num_words=5):
        for i in a:
            print (i)


doc_setScifi = processDirScifi('.')    
topic_modelingScifi(doc_setScifi)


#Horror
def processFileHorror(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        #print(file)
        text = f.read()
        #print(len(text))
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


def processDirHorror(dir):
    doc_setHorror = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Horror'):
            doc_setHorror.append(processFileHorror(file))
    return doc_setHorror

        
def topic_modelingHorror(doc_setHorror):
    #print(len(doc_setHorror))
    dictionary = corpora.Dictionary(doc_setHorror)
    corpus = [dictionary.doc2bow(text) for text in doc_setHorror]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=4, num_words=5):
        for i in a:
            print (i)


doc_setHorror = processDirHorror('.')    
topic_modelingHorror(doc_setHorror)


#Detectives
def processFileDetectives(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        #print(file)
        text = f.read()
        #print(len(text))
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


def processDirDetectives(dir):
    doc_setDetectives = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Detectives'):
            doc_setDetectives.append(processFileDetectives(file))
    return doc_setDetectives

        
def topic_modelingDetectives(doc_setDetectives):
    #print(len(doc_setDetectives))
    dictionary = corpora.Dictionary(doc_setDetectives)
    corpus = [dictionary.doc2bow(text) for text in doc_setDetectives]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=4, num_words=5):
        for i in a:
            print (i)


doc_setDetectives = processDirDetectives('.')    
topic_modelingDetectives(doc_setDetectives)


#Cyber
def processFileCyber(file): 
    doc = []
    with open (file, 'r', encoding='utf-8') as f:
        #print(file)
        text = f.read()
        #print(len(text))
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


def processDirCyber(dir):
    doc_setCyber = []
    dirlist = os.listdir(dir)
    for file in dirlist:
        if file.endswith('proc.txt') and file.startswith('Cyber'):
            doc_setCyber.append(processFileCyber(file))
    return doc_setCyber

        
def topic_modelingCyber(doc_setCyber):
    #print(len(doc_setCyber))
    dictionary = corpora.Dictionary(doc_setCyber)
    corpus = [dictionary.doc2bow(text) for text in doc_setCyber]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word = dictionary, passes=20)
    ldamodel[corpus]
    print ("\n\ntopics\n\n")
    for a in ldamodel.show_topics(num_topics=4, num_words=5):
        for i in a:
            print (i)


doc_setCyber = processDirCyber('.')    
topic_modelingCyber(doc_setCyber)