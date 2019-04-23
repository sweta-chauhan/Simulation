import numpy as np
import random_generator as rd
import plotter as pt

class Geometric_Random_Variate_Generator:
    def __init__(self,size,p,q,r_generator):
        self.size=size
        self.p=p
        self.r_generator = r_generator
        self.q = q
    def __iter__(self):
        return self
    def __next__(self):
        if(self.size==0):
            raise StopIteration
        self.size-=1
        return self.q + np.ceil((np.log(1-next(self.r_generator))/np.log(1-self.p))-1)


def geometric_generator(size,p,q):
    ls = Geometric_Random_Variate_Generator(size,p,q,rd.rand())
    return list(ls)
#print(geometric_generator(100,0.5,1))

def geo_parameter_estimator(data,size):
    return 1/np.mean(data),min(data) # p = 1/mean and (X>= q)=> q = min(data)
'''
ls=geometric_generator(500,.7,5)
print(ls)
pt.plot_it(ls,len(ls))
x,y=pt.calc_frequency_table(ls,10)
pt.histogram(x,y,"x","y")
'''
