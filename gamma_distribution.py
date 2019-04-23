'''

Parameter of gamma distribution is estimated by looking at Table.

I am generating gamma variate using acceptance and rejection technique.

'''

import numpy as np
import random_generator as rd
import plotter as pt
'''import reader as r
import matplotlib.pyplot as plt
from scipy.stats import gamma
'''

class Gamma_Random_Variate_Generator:
    def __init__(self,size,alpha,beeta,r_generator):
        self.size=size
        self.alpha=alpha
        self.a = 1/np.power((2*beeta-1),0.5)
        self.b = beeta-np.log(4)
        self.r_generator = r_generator
        self.beeta=beeta
    def __iter__(self):
        return self
    def __next__(self):
        if(self.size==0):
            raise StopIteration
        self.size-=1
        R1 = next(self.r_generator)
        R2 = next(self.r_generator)
        V  = R1/(1-R1)
        X = self.beeta*np.power(V,self.a)
        #print(self.p,np.exp(-self.alpha))
        while(X > self.b+(self.beeta*self.a+1)*np.log(V)-np.log((R1**2)*R2)):
            R1 = next(self.r_generator)
            R2 = next(self.r_generator)
            V  = R1/(1-R1)
            X = self.beeta*np.power(V,self.a)
        return X

def finding_T(data,size):
    return np.log(np.mean(data))-(1/size)*sum([map(lambda x:np.log(x),data)])
                                                                                
#After finding the value of T we have to find alpha,beeta corresponding value of 1/T

def gamma_parameter_estimator(data,size):
    var = np.var(data)
    mean = np.mean(data)
    beta = var/mean
    alpha = mean/beta
    #print(alpha,beta)
    return np.ceil(alpha),beta


def gamma_rand_gen(size,alpha,beeta):
    l = Gamma_Random_Variate_Generator(size,alpha,beeta,rd.rand())
    return list(l)

def fact(n):
    if(n==0.0 or n==1.0):
        return 1
    return n*fact(n-1)
def pdf(alpha,beta,a1):
    return np.power(beta,-alpha)*np.power(a1,alpha-1)*np.exp(a1/beta)/fact(alpha)

def integrate(alpha,beta,a1,a2,steps): 
    return 0.5*(pdf(alpha,beta,a2)-pdf(alpha,beta,a1))
 #print(gamma_rand_gen(10,2.10,2.30))
'''
ls=gamma_rand_gen(500,6,1.5)
pt.plot_it(ls,len(ls))
x,y=pt.calc_frequency_table(ls,10)
pt.histogram(x,y,"x","y")
'''
