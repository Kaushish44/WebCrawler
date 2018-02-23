'''
Created on 23-Feb-2018

@author: Aditya Kaushish
'''
from urllib.parse import urlparse

def get_domain(url):
    results = get_sub_domain(url).split('.')
    return results[-2] + '.' + results[-1]

def get_sub_domain(url):
    return urlparse(url).netloc
