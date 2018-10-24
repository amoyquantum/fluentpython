# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 08:45:37 2018

@author: Administrator
"""

import contextlib

@contextlib.contextmanager
def looking_glass(): 
    import sys
    original_write = sys.stdout.write
    
    def reverse_write(text):
        original_write(text[::-1])
    
    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write