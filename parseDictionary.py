import os
import json
import string

class dictionary(object):
    def myNo(self):
        self.domains=0;
        pass

    def __init__(self):
        dictionary_file = open("wordlist.json","r")
        self.s = json.load(dictionary_file)
        pass

    def search(self, word):
        wd = self.s['wordlist'].get(word)
        if wd is None:
            print word
            print "\tnot found"
        else:
            print word
            print "\t"+wd['pronunciation']
            print "\t"+wd['meaning']
    	pass



