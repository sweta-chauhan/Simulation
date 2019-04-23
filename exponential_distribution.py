'''A random variable x is said to be an exponential distribution with parameter lambda>0, if it's PDF is given by
                            { lambda *exp(-lambda*x) ; x>=0
             f(x)           {
                            {
                            { 0 ; otherwise


distribution function 
(CDF)

F(x) = P(X>=x) 
               =     x
                     | f(x)dx
                    -inf
               
               =    1-exp(-lambda*x)

'''



import numpy as np
import random_generator as rd
import plotter as pt
#Class for exponential random variate generator

class Exponential_Random_Variate_Generator:
    def __init__(self,size,lamda,r_generator):
        self.size=size
        self.lamda=lamda
        self.r_generator = r_generator
    def __iter__(self):
        return self
    def __next__(self):
        if(self.size==0):
            raise StopIteration
        self.size-=1
        return (-1/self.lamda)*np.log(next(self.r_generator))
        
def pdf(lamda,a1,a2,step):
    steps =(a2-a1)/step
    const = lamda*steps/2
    summing_part = 0.0
    i = 1
    while(i<step):
        summing_part+=np.exp(-lamda*(a1+i*steps))
        i+=1
    summing_part = const*(2*summing_part+np.exp(-lamda*a1)+np.exp(-lamda*a2))
    return summing_part

def integrate(beta,l_lim,u_lim,step):
    return pdf(1/beta,l_lim,u_lim,step)
    
def exponential_parameter_estimator(data):
    return np.mean(data)


#function to generate list of exponential random variate

def expon_rand_gen(size,lamda):
    l = Exponential_Random_Variate_Generator(size,lamda,rd.rand())
    return list(l)


#for i in l:
#    print(i)
'''
ls=expon_rand_gen(500,2)
print(expon_rand_gen(500,2))
pt.plot_it(ls,500)
x,y=pt.calc_frequency_table(ls,10)
pt.histogram(x,y,"x","y")
'''
'''
import sys as s
import reader as r
import plotter as p
if __name__ =='__main__':
    try:
        assert(len(s.argv)>=2)
    except:
        print("Please insert file name")
        print("May be specified is reside in your system")
    x=r.read_file(s.argv[1])
    p.plot_it(x,len(x))
'''
