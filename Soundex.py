#!/usr/bin/python
'''
Created on 20 Sep 2013

@author: mariaz
'''
from collections import defaultdict

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
    
    If first consonant is repeated, it should still be only coded as one value (i.e. as the first letter)
    >>> soundex('FFOOOOFF')
    'F100'
    
"""

    letterValues = defaultdict(lambda: "", 
                               {'A': '',
                                'B': '1', 'P': '1', 'F': '1', 'V': '1',
                                'C': '2', 'G': '2', 'J': '2', 'K': '2',
                                'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
                                'D': '3', 'T': '3',
                                'L': '4',
                                'M': '5', 'N': '5',
                                'R': '6',
                                
                                })
    
    aString = aString.upper()
    firstLetter = aString[:1]  # first character is dealt with specially
    coded = [letterValues[c] for c in list(aString)]
    
    prev = ''
    duplicate_free = []
    for x in coded:
        if x != prev:
            prev = x
            duplicate_free += x
            
    coded = duplicate_free[1:]
    
    return firstLetter + ''.join(coded + list('000'))[:3]
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
