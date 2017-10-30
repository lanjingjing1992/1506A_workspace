#coding=utf-8
import re
def f(language):
    # pattern = re.compile(r'<!DOCTYPE html>(.*?)<html>',re.I | re.M)
    pattern=re.compile('<span>([\\s\\S]*?)</span>' )
    items = re.findall(pattern, language)
    for item in items:

        for it in item:
           pat=re.compile('<img[^>]*/>')
           i = re.findall(pat, it)
           print i


#方法测试
language = '''<!DOCTYPE html>hello<html>'''
# f(language)