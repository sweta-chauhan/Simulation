'''
It is a discrete probability distribution.

f(x) = (exp(-lamda*t)*(lamda*t)^x)/x!

For generating poission_distribution. I am going to use acceptance-rejection technique.

'''
import numpy as np
import random_generator as rd
import plotter as pt
class Poission_Random_Variate_Generator:
    def __init__(self,size,alpha,r_generator):
        self.size=size
        self.alpha=alpha
        self.r_generator = r_generator
        self.p  = 1
        self.n = 0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.size==0):
            raise StopIteration
        self.size-=1
        self.p *= next(self.r_generator)
        #print(self.p,np.exp(-self.alpha))
        while(self.p >= np.exp(-self.alpha)):
            self.n+=1
            self.p *= next(self.r_generator)
        rand = self.n
        self.n = 0
        self.p = 1
        return rand
            
        
def poission_rand_gen(size,alpha):
    l = Poission_Random_Variate_Generator(size,alpha,rd.rand())
    return list(l)

#print(poission_rand_gen(10,4))
'''
ls=poission_rand_gen(500,10)
pt.plot_it(ls,len(ls))
x,y=pt.calc_frequency_table(ls,10)
pt.histogram(x,y,"x","y")
'''
