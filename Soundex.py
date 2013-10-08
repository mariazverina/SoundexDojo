#!/usr/bin/python
'''
Created on 20 Sep 2013

@author: mariaz
'''
from collections import defaultdict
import timeit

def soundex(aString):
    """Return the soundex value of a string. This is 4 character string with one alpha and 3 digits.

    One letter strings are just initial character and three zeros
    >>> soundex('M')
    'M000'
    
    Even vowel should be shown at start of the string
    >>> soundex('A')
    'A000'

    Vowels except first one should be dropped
    >>> soundex('KAAAA')
    'K000'
    
    Two consonants in different groups should be mapped to first letter + 1 number + two zeroes
    >>> soundex('RB'), soundex('RF'), soundex('RP'), soundex('RV')
    ('R100', 'R100', 'R100', 'R100')
    
    Two consonants in different groups should be mapped to first letter + 1 number + two zeroes
    Convert: b, f, p, v => 1
    >>> soundex('RB'), soundex('RF'), soundex('RP'), soundex('RV')
    ('R100', 'R100', 'R100', 'R100')
    
    We should treat all letters as capitals
    >>> soundex('rb')
    'R100'
    
    Convert: c, g, j, k, q, s, x, z => 2
    >>> [soundex('r'+x) for x in "c, g, j, k, q, s, x, z".split(", ")]
    ['R200', 'R200', 'R200', 'R200', 'R200', 'R200', 'R200', 'R200']
    
    Convert: d, t => 3
    >>> soundex('fd'), soundex('ft')
    ('F300', 'F300')
    
    Convert: l => 4
    >>> soundex('cl')
    'C400'
    
    Convert: m, n => 5
    >>> soundex('fm'), soundex('fn')
    ('F500', 'F500')

    Convert: r => 6
    >>> soundex('cr')
    'C600'
    
    Drop: a, e, i, o, u, y, h, w
    >>> soundex('caeiouyhwr')
    'C600'

    Two letters with same code separated by a vowel should be coded separately
    >>> soundex('FOOFOOFOOF')
    'F111'
    
    Repeated consonants with same value should only be coded as one value
    >>> soundex('ZAPF')
    'Z100'
    
    Repeated consonant rule also applies to the first letter
    >>> soundex('FFOOOOFF')
    'F100'
    
    Two letters with the same number separated by 'h' or 'w' are coded as a single number, 
    whereas such letters separated by a vowel are coded twice.
    >>> soundex('RWRHRWR')
    'R000'
    
    If first letter is a vowel, do not strip the first consonant
    >>> soundex('AS')
    'A200'
    
    Using this algorithm, both "Robert" and "Rupert" return the same string "R163" while 
    "Rubin" yields "R150". "Ashcraft" and "Ashcroft" both yield "A261" and not "A226" 
    (the chars 's' and 'c' in the name would receive a single number of 2 and not 22 
    since an 'h' lies in between them). "Tymczak" yields "T522" not "T520" (the chars 'z' 
    and 'k' in the name are coded as 2 twice since a vowel lies in between them). 
    "Pfister" yields "P236" not "P123" (the first two letters have the same number and
    are coded once as 'P').
    >>> soundex('Robert'), soundex('Rupert')
    ('R163', 'R163')
    >>> soundex('Ashcraft'), soundex('Ashcroft')
    ('A261', 'A261')
    >>> soundex('Tymczak')
    'T522'
    >>> soundex('Pfister')
    'P236'

    Careful not to strip off the first consonant when H/W disappear
    >>> soundex('wryly')
    'W640'
    >>> soundex('hry')
    'H600'

"""

    letterValues = defaultdict(lambda: "", 
                               {'H': "delete", "W": "delete",
                                # vowels are encoded as empty strings by the power of defaultdict
                                'B': '1', 'P': '1', 'F': '1', 'V': '1',
                                'C': '2', 'G': '2', 'J': '2', 'K': '2',
                                'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
                                'D': '3', 'T': '3',
                                'L': '4',
                                'M': '5', 'N': '5',
                                'R': '6',
                                
                                })
    
    aString = aString.upper()                                                       # strings must be upper case
    coded = [letterValues[c] for c in list(aString) if letterValues[c] != "delete"] # encode values & strip H/W
    
    duplicate_free = [a for (a,b) in zip(coded, [None] + coded) if a != b]          # drop duplicate values
    coded = [aString[:1]] + duplicate_free + list("000")                            # don't encode first character and pad with zeros
    if letterValues[coded[0]] == coded[1]:
        del coded[1]

    return ''.join(coded)[:4]                                                       # trim to 4 chars
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
