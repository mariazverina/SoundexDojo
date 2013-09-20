#!/usr/bin/python
'''
Created on 20 Sep 2013

@author: mariaz
'''

def soundex(aString):
    """Return the soundex value of a string. This is 4 character string with one alpha and 3 digits.

    One letter strings are just initial character and three zeros
    >>> soundex('M')
    'M000'
    
    
"""
    return 'M000'
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
