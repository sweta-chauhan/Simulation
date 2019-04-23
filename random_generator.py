'''

It's pseudo random number generator.

'''
import numpy as np
import sys as s

class LCG_Generator:
    def __init__(self,m,a,c,zi):
        self.ui=0
        self.zi=zi
        self.a=a
        self.c=c
        self.m=m
        self.first = ((self.a*self.zi)+self.c)%self.m
        self.flag = 1
        #print(self.ui,self.zi,self.a,self.c,self.m,self.first)
    def __iter__(self):
        return self

    def __next__(self):
        z1=((self.a*self.zi)+self.c)%self.m
        #print(self.ui,self.zi,self.a,self.c,self.m,self.first)
        if(self.flag!=1):
            #print(self.ui,self.zi)
            if z1 == self.first:
                raise StopIteration
        self.flag = 0
        self.ui = z1/self.m # ui = z1/m
        self.zi=z1
        z1=((self.a*self.zi)+self.c)%self.m
        return self.ui

        
        

def rand():
    gen = LCG_Generator(2147483647,22695477,1,2**30)
    return gen
'''
gen = rand()
for i in gen:
        print(i)
'''
'''
def generate_random_lcg(m,a,c,zi):
    list1=[]
    ui = []
    z1=((a*zi)+c)//m
    while(z1 not in list1):
        list1.append(z1)
        ui.append(z1/m)
        zi=z1
        z1=((a*zi)+c)%m
    print(ui,list1)
    return ui
'''
if __name__ =='__main__':
    x =LCG_Generator(2147483647,123,789,456)
    
    for i in x:
        print(i)
    #plot_it(x)
    #print(find_variance(x))

