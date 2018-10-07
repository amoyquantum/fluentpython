# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 12:20:00 2018

@author: Administrator
"""

from clockdeco import clock
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
if __name__=='__main__':
    print(fibonacci(6))