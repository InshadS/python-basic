import ari 

def test_ari_numcharacter():
     ret=ari.ari_numcharacter('hello123')
     assert ret==8

def test_ari_emptywords():
     ret=ari.ari_emptyword('qwerty')
     assert ret==None

def test_ari_numword():
     ret=ari.ari_numword('see you next time')
     assert ret==3

def test_ari_emptysentence():
     ret=ari.ari_emptysentence('this is not a sentence')
     assert ret==None

def test_ari_sentence():
     ret=ari.ari_sentences('I get it! I can’t even read what I was writing before. Can you write something?')
     assert ret==3