'''

It is normally used to predict time to failure for machine or electronic components.

alpha scale parameter
beeta shape parameter
        {
f(x) =  {
        {
        
        {
F(x)=   { 1-exp(-(x/alpha)^beeta)
        {

let X be random variate
then 
    X = alpha*(-ln(Ui))^(1/beeta)


Note :-

if X is weibull variate then X^beeta is exp(alpha^beeta).
Conversely, if Y is an exponential variate with mean mhu then Y^(1/beeta) is weibull variate with shape parameter beeta and scale parameter alpha = mhu^(1/beeta).


'''

import numpy as np
import random_generator as rd
import plotter as pd
class Weibull_Random_Variate_Generator:
    def __init__(self,size,alpha,beeta,r_generator):
        self.size=size
        self.alpha=alpha
        self.r_generator = r_generator
        self.beeta = beeta
    def __iter__(self):
        return self
    def __next__(self):
        if(self.size==0):
            raise StopIteration
        self.size-=1
        return self.alpha*[-np.log(next(self.r_generator))]**(1/self.beeta)


def weibull_rand_gen(size,alpha,beeta):
    l = Weibull_Random_Variate_Generator(size,alpha,beeta,rd.rand())
    return list(l)

def func(data,beeta,n,ln_sum):
    x1=list(map(lambda x:np.power(x,beeta)*np.log(x),data))
    x2=list(map(lambda x:np.power(x,beeta),data))
    return (n/beeta)+ln_sum+n*(sum(x1))/(sum(x2))

def func_differenciation(data,beeta,n):
    f1 = -n/beeta
    x1 = sum([map(lambda x:np.power(x,beeta)),data])
    x2=list(map(lambda x:np.power(x,beeta)*(np.log(x)**2),data))
    f2 = n*(sum(x2)/x1)
    x3=sum(list(map(lambda x:np.power(x,beeta)*np.log(x),data)))
    f3 = n*np.power(x3,2)/np.power(x1,2)
    return f1-f2+f3

def weibull_parameter_estimator(data,size):
    i_beta = np.mean(data)/np.std(data)
    i1_beta = 0.0
    l = list(map(lambda x: np.log(x),data))
    ln_sum = sum(l)
    while(np.abs(func(data,i_beta,size,ln_sum))<=0.001):
        i1_beta = i_beta - func(data,i_beta,size,ln_sum)/func_differenciation(data,i_beta,size)
        i_beta = i1_beta
    alpha = np.power(sum(data)/size,1/i_beta)
    return alpha,i_beta 


#weibull_parameter_estimator()
'''
ls=weibull_rand_gen(500,2,3.5)
pt.plot_it(ls,len(ls))
x,y=pt.calc_frequency_table(ls,10)
pt.histogram(x,y,"x","y")
'''
