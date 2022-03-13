import math

def ari_numcharacter(s):
     acc=0
     for i in s:
          acc+=1
     return acc


def ari_emptyword(s):
     if " " not in s:
          return None


def ari_numword(s):
     acc=0
     for i in s:
          if i ==' ':
               acc+=1
     return acc


def ari_emptysentence(s):
     if "." or "!" or "?" not in s:
          return None


def ari_sentences(s):
     acc=0
     for i in s:
          if i == '!' or i == '?' or i == '.':
               acc+=1
     return acc


def ari_calculation(string):
     index= math.ceil(4.71*(ari_numcharacter(string)//ari_numword(string))+0.5*(ari_numword(string)//ari_sentences(string))-21.43)
     dict={
          1:"5-6 Kindergarten",
          2:"6-7 First Grade",
          3:"7-8 Second Grade",
          4:"8-9 Third Grade",
          5:"9-10 Fourth Grade",
          6:"10-11 Fifth Grade",
          7:"11-12 Sixth Grade",
          8:"12-13 Seventh Grad",
          9:"13-14 Eighth Grade",
          10:'14-15	Ninth Grade',
          11:'15-16	Tenth Grade',
          12:'16-17	Eleventh Grade',
          13:'17-18	Twelfth Grade',
          14:'18-22	College student'
          } 
     return dict[index]

