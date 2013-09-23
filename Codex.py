'''
Created on 23 Sep 2013

@author: mariaz
'''

import Soundex

if __name__ == '__main__':
    with open("/usr/share/dict/words") as f:
        for line in f:
            line = line.strip()
            print line, "->", Soundex.soundex(line)
