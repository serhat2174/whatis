import wikipedia
import termcolor
from termcolor import colored
import sys
import os
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
os.system('color')
while True:
    q=(colored('\nWhat is?: ','green'))
    d=input (q)
    try:
        p= wikipedia.summary(d, sentences=5)
        t= wikipedia.page(d)
        print(colored(t.title+": ",attrs=['bold']))
        print(p)
    except:
        try:
            d1=d.replace(" ","")
            p= wikipedia.summary(d1, sentences=4)
            t= wikipedia.page(d)
            print(colored(t.title+": ",attrs=['bold']))
            print(p)   
        except:
            try:
                d2=("a "+d)
                p= wikipedia.summary(d2, sentences=4)
                t= wikipedia.page(d2)
                print(colored(t.title+": ",attrs=['bold']))
                print(p)
                #print(colored(p,attrs=['bold']))   
            except:
                s=wikipedia.search(d)
                print("\nNo record. \nTry:\n"+str(s))
                continue

    if True:
            continue
