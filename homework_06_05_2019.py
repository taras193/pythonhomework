phylosophy='''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
#1
result_better=phylosophy.find('better')
print('''There are "better":''', result_better)

result_never=phylosophy.find('never')
print('''There are "never":''', result_never)
#2
upper_string = phylosophy.upper()
print(upper_string)
#3
replaced_string=phylosophy.replace('i','&')
print (replaced_string)

