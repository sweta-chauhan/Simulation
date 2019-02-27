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



if __name__ =='__main__':
    try:
        assert(len(s.argv)>=2)
    except:
        print("Please insert file name")
        print("May be specified is reside in your system")
    x=r.read_file(s.argv[1])
    p.plot_it(x,len(x))


