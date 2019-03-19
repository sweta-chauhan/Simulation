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
import sys as s
import reader as r
import plotter as p

def pdf(lamda,a1,a2,step):
    steps = lamda*((a2-a1)/(2*step))
    summing_part = 0.0
    i = 1
    while(i<step):
        summing_part+=np.exp(-lamda*(a1+i*steps))
        i+=1
    summing_part = steps*(2*summing_part+np.exp(-lamda*a1)+np.exp(-lamda*a1))
    #print(summing_part)
    return summing_part
def integrate(beta,l_lim,u_lim,step):
    return pdf(1/beta,l_lim,u_lim,step)
    
def exponential_parameter_estimator(data):
    return np.mean(data)




'''if __name__ =='__main__':
    try:
        assert(len(s.argv)>=2)
    except:
        print("Please insert file name")
        print("May be specified is reside in your system")
    x=r.read_file(s.argv[1])
    p.plot_it(x,len(x))


'''
