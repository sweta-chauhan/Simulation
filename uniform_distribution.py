import random_generator as r
import numpy as np
import sys as s
import reader as rd

class Uniform_Random_Variate_Generator:
    def __init__(self,a,b,size,r_generator):
        self.size=size
        self.a=a
        self.b=b
        self.r_generator = r_generator
    def __iter__(self):
        return self
    def __next__(self):
        if(self.size==0):
            raise StopIteration
        self.size-=1
        return self.a+next(self.r_generator)*(self.b-self.a)

def uni_rand_gen(size,a,b):
    l = Uniform_Random_Variate_Generator(a,b,size,r.rand())
    return list(l)

def estimator_of_uniform_distribution(data):
    mean,var = np.mean(data),np.var(data)
    b = (2*mean+np.sqrt(12*var))/2
    return b,2*mean-b


#print(uni_rand_gen(10,2,5))

'''def uniform_generator(a,b,size):
    gen = r.rand()
    ls = []
    while(size<500):

        print(next(gen))
        #next(gen)
        size+=1
        ls.append()

a,b=estimator_of_uniform_distribution(np.array(rd.read_csv('2_2.csv')))
print(a,b)
#uniform_generator(a,b,0)
'''
