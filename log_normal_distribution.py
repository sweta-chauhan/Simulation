'''A random variable x is said to be an exponential distribution with parameter mhu E R, if it's PDF is given by
                            { (1/(sigma*sqrt(2*pi)))*exp(-((ln(x)-mhu)**2)/2*sigma) ; x>0
             f(x)           {
                            {
                            { 0 ; otherwise


it's right skewed unimodel function
distribution function 
(CDF)

F(x) = P(X>=x) 
               = x
                     | f(x)dx
                    -inf
     

'''

import numpy as np
import random_generator as rd
import plotter as pt

class LogNormal_Random_Variate_Generator:
    def __init__(self,size,mhu,sigma,r_generator):
        self.size=size
        self.mhu=mhu
        self.r_generator = r_generator
        self.sigma = sigma
    def __iter__(self):
        return self
    def __next__(self):
        if(self.size==0):
            raise StopIteration
        self.size-=1
        value = (np.sqrt(-2*np.log(next(self.r_generator))))*(np.cos(2*np.pi*next(self.r_generator)))
        return np.exp(self.mhu + self.sigma*value)

def log_normal_generator(size,mhu,sigma):
    mhu = np.log((mhu**2)/np.sqrt(mhu**2+sigma**2))
    sigma = np.log((mhu**2+sigma**2)/(mhu**2))
    ls = LogNormal_Random_Variate_Generator(size,mhu,sigma,rd.rand())
    return list(ls)

#print(log_normal_generator(10,50,9))
def log_normal_parameter_estimator(data):
    mean = np.mean(data)
    size = len(data)
    mhu_ = sum(map(lambda x:np.log(x),data))/size
    return mhu_,sum(map(lambda x: np.square(np.log(x)-mhu_),data))/size


def cdf(mhu_,sigma,l_limit,u_limit,step):
    steps = (u_limit-l_limit)/(step)
    const = (1/(np.sqrt(2*mhu_*sigma*np.pi)))*(steps/2)
    #print(1/(np.sqrt(2*mhu_*sigma*np.pi)))
    summing_part = 0.0
    i = 1
    while(i<step):
        summing_part+=np.exp(-(np.square(np.log(l_limit+i*steps)-mhu_))/(2*sigma))
        i+=1
    summing_part = const*(2*summing_part+np.exp(-0.5*(np.square(np.log(l_limit)-mhu_))/sigma)+np.exp(-0.5*(np.square(np.log(u_limit)-mhu_))/sigma))
    return summing_part

def integrate(mhu_,sigma,l_limit,u_limit,step):
    #print(mhu_,sigma,l_limit,u_limit,step)
    return cdf(mhu_,sigma,l_limit,u_limit,step)


'''print(log_normal_parameter_estimator([4.96220170720832, 9.31566269994964, 13.66912369269096, 18.022584685432278, 22.376045678173597, 26.729506670914915, 31.082967663656234, 35.43642865639755, 39.78988964913887, 44.14335064188019, 48.49681163462151, 52.85027262736283, 57.203733620104146, 61.557194612845464, 65.91065560558678, 70.2641165983281, 74.61757759106942, 78.97103858381074, 83.32449957655206, 87.67796056929338, 92.0314215620347, 96.38488255477601, 100.73834354751733, 105.09180454025865, 109.44526553299997, 113.79872652574129]))
'''
ls=log_normal_generator(1000,2.5,5)
pt.plot_it(ls,len(ls))
x,y=pt.calc_frequency_table(ls,10)
pt.histogram(x,y,"x","y")
