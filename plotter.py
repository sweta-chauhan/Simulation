import matplotlib.pyplot as plt
import sys as s
import reader as r

def plot_it(x,size):
    y = x[1:]+[x[-1]]
    plt.scatter(x,y,marker='p')
    plt.show()
    return True

def calc_frequency_table(ls,interval_size):
    max1,min1 = max(ls),min(ls)
    prev1 = min1
    x = []
    step= (max1-min1)/interval_size
    min1+=step
    while(min1<=max1):
        x.append(min1)
        min1+=step
    #print(min1>x[-1],max1>x[-1],max1,min1,x[-1])
    if(max1>x[-1]):
        x.append(max1+1)
    len1=len(x)
    count = 0
    y = []
    for i in range(len1):
        for j in ls:
            if(prev1<=j and j<x[i]):
                count+=1
        prev1=x[i]
        y.append(count)
        count =0
    print(len(y),len(x),len(ls))
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
    x,y=calc_frequency_table(x,int(s.argv[2]))
    histogram(x,y,"x_axis","y_axi")
