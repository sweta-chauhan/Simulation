import matplotlib.pyplot as plt
import sys as s
import reader as r

def plot_it(x,size):
    y = x[1:]+[x[-1]]
    plt.scatter(x,y,marker='o')
    plt.show()
    return True

def calc_frequency_table(ls,interval_size):
    max1,min1 = max(ls),min(ls)
    x = []
    step= (max1-min1)/interval_size
    while(min1<=max1):
        x.append(min1)
        min1+=step
    if(min1<max1):
        x.append(min1+1)
    len1=len(x)
    count = 0
    y = []
    for i in range(1,len1):
        for j in ls:
            if(x[i-1]<=j and j<x[i]):
                count+=1
        y.append(count)
        count =0
    for j in ls:
        if (x[-1]<=j and j<x[-1]+1):
            count+=1
    y.append(count)
    return x,y


def histogram(x,y,xlabel,ylabel):
    plt.plot(x,y,color='red')
    plt.bar(x,y,width=0.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return True




if __name__ =='__main__':
    try:
        assert(len(s.argv)>=2)
    except:
        print("Please insert file name")
        print("May be specified is reside in your system")
    x=r.read_csv(s.argv[1])
    plot_it(x,len(x))
    #x,y=calc_frequency_table(x,11)
    #histogram(x,y,"x_axis","y_axi")
