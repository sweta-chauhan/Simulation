import sys as s
import numpy as np

import reader as r
import uniform_distribution as ud
import exponential_distribution as ed
import plotter as plt

chi_square_tab = r.read_csv_two_col('chi_square_table_with_05_significance.csv')

def uniform_dist_chi_square_test(data,size,interval):
    min1,max1 = float(min(data)),float(max(data))
    step = float((max1-min1)/interval)
    prev1=0.0
    next1=min1
    ai = []
    oj=[]
    vari = []
    b,a = ud.estimator_of_uniform_distribution(data)
    
    #ej = float(size/(b-a))
    ej = float(size/interval)
    #print(ej)
    while(next1<=max1):
        prev1=next1
        next1=next1+step
        ai.append(next1)

    prev1 = min1
    count = 0.0

    for _ in ai:
        count=0.0
        #print(prev1,_)
        for i in data:
            if(i>=prev1 and i<_):
               count+=1.0
        prev1 = _    
        oj.append(count)

    for i in oj:
        vari.append(np.square(i-ej)/ej)
    #print(sum(vari))
    return ai,oj,ej,vari,sum(vari)

def merge_interval(beta,ai,oj,ej,val,prev1,i,interval):
    current_ptr = i
    prev1=ai[i]
    while(val<=5 and i<interval-1):
        i+=1
        ai[current_ptr]=ai[i]
        oj[current_ptr]+=oj[i]
        val+= size*ed.integrate(beta,prev1,ai[i],100)
        prev1=ai[i]
    if(val<5 and (i-1)>=0):
        val += size*ed.integrate(beta,ai[i-1],ai[current_ptr],100)
        ai[i-1]=ai[current_ptr]
        oj[i-1]+=oj[current_ptr]
        return ai[0:current_ptr+1],oj[0:current_ptr+1],val,current_ptr
    return ai[0:current_ptr+1]+ai[i:],oj[0:current_ptr+1]+oj[i:],val,current_ptr

def exponential_dist_chi_square_test1(data,size,interval):
    min1,max1 = float(min(data)),float(max(data))
    step = float((max1-min1)/interval)
    prev1=0.0
    next1=min1
    ai = []
    oj=[]
    ej=[]
    vari = []
    beta = ed.exponential_parameter_estimator(data)
    while(next1<=max1):
        prev1=next1
        next1=next1+step
        ai.append(next1)
    prev1 = min1
    count = 0.0
    for _ in ai:
        count=0.0
        for i in data:
            if(i>=prev1 and i<_):
               count+=1.0
        prev1 = _    
        oj.append(count)
        prev1=min1
        i = 0
        ej.append(val)
        prev1=ai[i]
        vari.append(np.square(val-oj[i])/val)
        i+=1
    return ai,oj,ej,vari,sum(vari)



#size = len(data)
#x,y,z,w=uniform_dist_chi_square_test(data,size,9)
#x,y,z,w=exponential_dist_chi_square_test1(data,size,25)

'''for i in w:
    print(i)
'''

def print_tab(x,y,w,z):
    try:
        assert(len(x)==len(y) and len(y)==len(z) and len(z)==len(w) and len(x)!=0)
    except:
        print("No table is formed")
        return False
    i=0
    while(i<len(x)):
        print(x[i],y[i],z[i],w[i])
        i+=1
    return True



def chi_square_test(calculated_val,parameters):
    if(calculated_val<=chi_square_tab[parameters]):
        return True
    return False
#plt.histogram(x,y,'x','y')

#chi_square_value(data,size,15)
#print(size*ed.integrate(1/np.mean(data),7.86,109.44526553300003,100))

if __name__ =='__main__':
    try:
        assert(len(s.argv)>2)
    except:
        print("filename and size is not specified !!")
    if('-h' in s.argv):
        print("Choose one option to perform respective distribution chi square test")
        print("1.  Uniform")
        print("2.  Exponential")
        print("3.  Log Normal")
        print("4.  Normal")
        print("5.  Weibull")
        print("6.  Gamma")
        print("7.  Poisson")
        print("8.  Geometric")
        print("9.  HyperGeometric")
        print("10. Binomial")
        print("11. Bernauli")
        print("12. Exit")
    ch = 0
    try:
        data = r.read_csv(s.argv[1])
    except:
        print("May be file doesn't exist or filename name is not specified in defined format")
        print("First specify filename then interval size")
    interval = float(s.argv[2])
    size = len(data)
    while(ch!=12):
        ch = int(input())
        if(ch ==1):
            x,y,z,w,val=uniform_dist_chi_square_test(data,size,interval)
            print(x)
            print(y)
            print(z)
            print(w)
            print("chi_suqare_value",val)
            res = chi_square_test(val,interval-3)
            if(res==True):
                print("Given data set is fitted in Uniform distribution.")
            else:
                print("Not fitted in Uniform distribution.")
        if(ch ==2):
            x,y,z,w,val=exponential_dist_chi_square_test1(data,size,interval)
            print(x)
            print(y)
            print(z)
            print(w)
            print("chi_suqare_value",val)
            res =chi_square_test(val,interval-2)
            if(res==True):
                print("Given data set is fitted in Exponential distribution.")
            else:
                print("Not fitted in Exponential distribution.")
        if(ch ==3):
            print("rest")
        if(ch ==4):
            print("rest")
        if(ch ==5):
            print("rest")
        if(ch ==6):
            print("rest")
        if(ch ==7):
            print("rest")
        if(ch ==8):
            print("rest")
        if(ch ==9):
            print("rest")
        if(ch ==10):
            print("rest")
        if(ch==11):
            print("rest")
