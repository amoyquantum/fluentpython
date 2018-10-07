# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:57:29 2018

@author: Administrator
"""

registry = set()
def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)'
                  % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate
@register(active=False)
def f1():
    print('running f1()')
@register()
def f2():
    print('running f2()')
def f3():
    print('running f3()')