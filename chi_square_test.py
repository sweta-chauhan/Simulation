#Python packages
import sys as s
import numpy as np

#my modules
import reader as r
import plotter as plt

import geometric_distribution as gmd
import poission_distribution as pd
#import hyperGeometric_distribution as hd
#import binomial_distribution as bd
#import negative_binaomial_distribution as nd

import uniform_distribution as ud
import exponential_distribution as ed
import log_normal_distribution as ld
import normal_distribution as nd
import gamma_distribution as gd
import weibull_distribution as wd
#import beta_distribution as bd
 

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
        #prev1=next1
        next1=next1+step
        ai.append(next1)
    #if(max1>ai[-1]):
     #   x.append(max1+1)
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

def uniform_dist(data,size,interval):
    p = float(1.0/interval)
    min1,max1 = min(data),max(data)
    j = 0
    ai=[]
    oj=[]
    var=[]
    ej=(size+1)*p
    b,a = ud.estimator_of_uniform_distribution(data)
    while(j<interval):
        #print(j)
        ai.append((j*p)*(b-a)+a)
        j+=1
    ai.append(max1+1.0)
    prev1 = min1
    for _ in ai:
        count=0.0
        for i in data:
            if(i>=prev1 and i<_):
               count+=1.0
        prev1 = _    
        oj.append(count)
    j = 0
    #print(min1,max1,ai[0],ai[-1])
    #print(sum(oj),len(oj),len(ai))
    for i in oj:
        var.append(np.square(i-ej)/ej)
        j+=1
    return sum(var)


def merge_interval(beta,ai,oj,ej,val,prev1,i,interval):
    current_ptr = i
    prev1=ai[i]
    print(ai,oj)
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
    return ai[0:current_ptr+1]+ai[i+1:],oj[0:current_ptr+1]+oj[i+1:],val,current_ptr

def exponential_dist_chi_square_test1(data,size,interval):
    min1,max1 = float(min(data)),float(max(data))
    step = float((max1-min1)/interval)
    prev1=0.0
    next1=min1+step
    ai = []
    oj=[]
    ej=[]
    vari = []
    beta = ed.exponential_parameter_estimator(data)
    while(next1<max1):
        ai.append(next1)
        next1=next1+step
    if(ai[-1]<max1 and len(ai)<interval):
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
    #print(len(ai),len(oj))
    while(i<interval and i<len(ai)):
        #print(i,prev1,ai[i])
       # print(i,interval)
        #print(val<5,val)
        val = (ed.integrate(beta,prev1,ai[i],100))*size
        #ej.append(val)
        #print(val<5,val)
        '''if(val<5):
            #print(val,"hello")
            #ai,oj,val,i = merge_interval(beta,ai,oj,ej,val,prev1,i,interval)
            ej.append(val)
            vari.append(np.square(val-oj[i])/val)'''
        #print(i,interval)
        #print(np.square(val-oj[i])/vari[i],oj[i],vari[i])
        '''else:
            vari.append(np.square(val-oj[i])/val)
            ej.append(val)
            i+=1
        '''
        
        #changes I am doing for merging
        #print(ej[i],i)
        ej.append(val)
        prev1=ai[i]
        vari.append(np.square(val-oj[i])/val)
        i+=1
    return sum(vari)

def log_normal_chi_square_test(data,size,interval):
    min1,max1 = float(min(data)),float(max(data))
    step = float((max1-min1)/interval)
    prev1=0.0
    next1=min1+step
    ai = []
    oj=[]
    ej=[]
    vari = []
    mhu,sigma = ld.log_normal_parameter_estimator(data)
    while(next1<max1):
        ai.append(next1)
        next1=next1+step
    if(ai[-1]<max1 and len(ai)<interval):
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
    while(i<interval and i<len(ai)):
        val = size*(ld.integrate(mhu,sigma,prev1,ai[i],100))
        ej.append(val*size)
        prev1=ai[i]
        vari.append(np.square(val-oj[i])/val)
        i+=1
    return sum(vari)

##Check it
def normal_chi_sqr_test(data,size,interval):
    min1,max1 = float(min(data)),float(max(data))
    step = float((max1-min1)/interval)
    prev1=0.0
    next1=min1+step
    ai = []
    oj=[]
    ej=[]
    vari = []
    mhu,sigma = nd.normal_parameter_estimator(data)
    while(next1<max1):
        ai.append(next1)
        next1=next1+step
    if(ai[-1]<max1 and len(ai)<interval):
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
    while(i<interval and i<len(ai)):
        val = size*(nd.integrate(mhu,sigma,prev1,ai[i],100))
        ej.append(val)
        prev1=ai[i]
        vari.append(np.square(val-oj[i])/val)
        i+=1
    return sum(vari)

def weibull_chi_sqr_test(data,size,interval):
    p = float(1.0/interval)
    min1,max1 = min(data),max(data)
    j = 0
    ai=[]
    oj=[]
    vari=[]
    ej = (size)*p
    beta,alpha = wd.weibull_parameter_estimator(data,size)
    while(j<interval):
        #print(j)
        ai.append((-np.log(1-j*p))**(1/alpha)*beta)
        j+=1
    ai.append(max1+1.0)
    prev1 = min1
    for _ in ai:
        count=0.0
        for i in data:
            if(i>=prev1 and i<_):
               count+=1.0
        prev1 = _    
        oj.append(count)
    j = 0
    #print(ai,oj,ej,p,size)
    for i in oj:
        vari.append(np.square(i-ej)/ej)
    return sum(vari)
def gamma_chi_sqr_test(data,size,interval):
    min1,max1 = float(min(data)),float(max(data))
    step = float((max1-min1)/interval)
    prev1=0.0
    next1=min1+step
    ai = []
    oj=[]
    ej=[]
    vari = []
    alpha,beta = gd.gamma_parameter_estimator(data,size)
    while(next1<max1):
        ai.append(next1)
        next1=next1+step
    if(ai[-1]<max1 and len(ai)<interval):
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
    while(i<interval and i<len(ai)):
        val = size*(gd.integrate(alpha,beta,prev1,ai[i],1))
        ej.append(val)
        prev1=ai[i]
        vari.append(np.square(val-oj[i])/val)
        i+=1
    return sum(vari)
    
def geometric_chi_sqr_test(data,size,interval):
    return True
def beta_chi_sqr_test(data,size,interval):
    return True
def poission_chi_sqr_test(data,size,interval):
    return True


def chi_square_test(calculated_val,parameters):
    try:
        if(calculated_val<=chi_square_tab[parameters]):
            return True
    except:
        print("Error : For given interval corresponding value is not found in table !!")
        return False

def find_intervals_in_which_distribution_fitted(choice,data):
    res = []
    for i in chi_square_tab:
        res.append(i)
    if(choice==1):
        #print(chi_square_test(uniform_dist_chi_square_test(data,len(data),1+3),1))
        res = [i+3 for i in res if chi_square_test(uniform_dist_chi_square_test(data,len(data),i+3),i)==True]
    if(choice==2):
        res = [i+2 for i in res if chi_square_test(exponential_dist_chi_square_test1(data,len(data),i+2),i)==True]
    if(choice==3):
        res = [i+3 for i in res if chi_square_test(log_normal_chi_square_test(data,len(data),i+3),i)==True]
    if(choice==4):
        res = [i+3 for i in res if chi_square_test(normal_chi_sqr_test(data,len(data),i+3),i)==True]
    if(choice==5):
        res = [i+3 for i in res if chi_square_test(weibull_chi_sqr_test(data,len(data),i+3),i)==True]
    #print(res)
    if(choice==6):
        res = [i+3 for i in res if chi_square_test(gamma_chi_sqr_test(data,len(data),i+3),i)==True]
        
    return res




if __name__ =='__main__':
    try:
        assert(len(s.argv)>=2)
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
        print("11. Negative Binaomial")
        print("12. Exit")
        print(chi_square_tab)
    ch = 0
    try:
        data = r.read_csv(s.argv[1])
    except:
        print("May be file doesn't exist or filename name is not specified in defined format")
        print("First specify filename then interval size")
    size = len(data)
    while(ch!=12):
        ch = int(input())
        if(ch ==1):
            interval = float(input("Enter interval size"))
            x,y,z,w,val=uniform_dist_chi_square_test(data,size,interval)
            #print(x)
            #print(y)
            #print(z)
            #print(w)
            print("chi_suqare_value "+str(val))
            res = chi_square_test(val,interval-3)
            plt.histogram(x,y,'x','y')
            '''if(res==True):
                print("Given data set is fitted in Uniform distribution.")
            else:
                print("Not fitted in Uniform distribution.")'''
            '''res = find_intervals_in_which_distribution_fitted(ch,data)
            if(len(res)>0):
                print("Given Data set is fitted with uniform distribution with following interval size :> ")
                print(res)
            else:
                print("Not fitted in Uniform distribution. :< ")'''
        if(ch ==2):

            interval = float(input("Enter interval size"))
            '''x,y,z,w,val=exponential_dist_chi_square_test1(data,size,interval)
            #print(x)
            #print(y)
            #print(z)
            #print(w)
            print(len(x),len(y),len(z),len(w))
            print("chi_suqare_value " + str(val))
            #plt.histogram(x,y,'x','y')
            res =chi_square_test(val,interval-3)
            if(res==True):
                print("Given data set is fitted in Exponential distribution.")
            else:
                print("Not fitted in Exponential distribution.")'''
            res = find_intervals_in_which_distribution_fitted(ch,data)
            if(len(res)>0):
                print("Given Data set is fitted with exponential distribution with following interval size :> ")
                print(res)
            else:
                print("Not fitted in exponential distribution. :< ")
        if(ch ==3):
            #print("rest")
            '''interval = float(input("Enter interval size"))
            x,y,z,w,val=log_normal_chi_square_test(data,size,interval)
            #print(x)
            #print(y)
            #print(z)
            #print(w)
            print(len(x),len(y),len(z),len(w))
            print("chi_suqare_value "+str(val))
            res =chi_square_test(val,interval-3)
            if(res==True):
                print("Given data set is fitted in Log Normal distribution.")
            else:
                print("Not fitted in Log Normal distribution.")'''
            
            res = find_intervals_in_which_distribution_fitted(ch,data)
            if(len(res)>0):
                print("Given Data set is fitted with log Normal distribution with following interval size :> ")
                print(res)
            else:
                print("Not fitted in Log Normal distribution. :< ")

        if(ch ==4):
            #print("rest")
            '''interval = float(input("Enter interval size"))
            x,y,z,w,val=log_normal_chi_square_test(data,size,interval)
            #print(x)
            #print(y)
            #print(z)
            #print(w)
            print(len(x),len(y),len(z),len(w))
            print("chi_suqare_value "+str(val))
            res =chi_square_test(val,interval-3)
            if(res==True):
                print("Given data set is fitted in Normal distribution.")
            else:
                print("Not fitted in Normal distribution.")'''
            
            res = find_intervals_in_which_distribution_fitted(ch,data)
            if(len(res)>0):
                print("Given Data set is fitted with NORMAL distribution with following interval size :> ")
                print(res)
            else:
                print("Not fitted in Normal distribution. :< ")
        if(ch ==5):
            interval = float(input("Enter interval size"))
            res = find_intervals_in_which_distribution_fitted(ch,data)
            if(len(res)>0):
                print("Given Data set is fitted with Weibull distribution with following interval size :> ")
                print(res)
            else:
                print("Not fitted in Normal distribution. :< ")
            #print(weibull_chi_sqr_test(data,size,interval))
        if(ch ==6):
            #interval = float(input("Enter interval size"))
            res = find_intervals_in_which_distribution_fitted(ch,data)
            if(len(res)>0):
                print("Given Data set is fitted with gamma distribution with following interval size :> ")
                print(res)
            else:
                print("Not fitted in gamma distribution. :< ")
            #print("rest")
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


#data = r.read_csv('2_1.csv')
#find_intervals_in_which_distribution_fitted(1,data)


'''
data = r.read_csv('2_1.csv')
size = len(data)
#a,b,c,d,v=uniform_dist(data,size,25)

#print(v)
#print(min(data))
#x,y,z,w,val=uniform_dist_chi_square_test(data,size,9)
#print(val)
#print(val,len(x),len(y),len(w))
x,y,z,w,val=log_normal_chi_square_test(data,size,25)
plt.histogram(x,y,'x','y')
print(val)
'''
#print(y,z)
#print(val,len(x),len(y),len(w),x[-1],max(data))
#i=0
#print(val,len(x),len(y),len(w))
#while(i<len(x)):
#    print(x[i],y[i],z[i],w[i],val)
#    i+=1

'''for i in w:
    print(i)
'''
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
'''

'''data = r.read_csv('2_1.csv')
print(find_intervals_in_which_distribution_fitted(3,data))
'''


#plt.histogram(x,y,'x','y')

#chi_square_value(data,size,15)
#print(size*ed.integrate(1/np.mean(data),7.86,109.44526553300003,100))
