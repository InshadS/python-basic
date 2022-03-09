from program import average, count, panagram

#Count
def test_single():
        ret = count("aaa")
        assert ret == {"a" : 3}

def test_Multiple():
        ret = count("aaabbcc")
        assert ret == {"a" : 3, "b" : 2, "c" : 2} 

def test_empty():
        ret = count("")
        assert ret == {}


#Panagram
def test_panagram_true():
        ret = panagram("the quick brown fox jumps over a lazy dog")
        assert ret == True       
        

def test_panagram_false():
        ret = panagram("the quick brown fox jumped over a lazy dog")
        assert ret == False


#Average
def test_average_positive():
        ret = average([1,2,3,4,5])
        assert ret == 3

def test_average_negetive():
        ret = average([-1,-2,-3,-4,-5])
        assert ret == -3

def test_average_none():
        ret = average([])
        assert ret == None
