import matplotlib.pyplot as plt
import numpy as np
import sys as s

def plot_it(x,size):
    y = x[1:]
    y=np.array(list(y)+[x[-1]])
    print(x,y)
    plt.scatter(x,y,marker='o')
    plt.show()
def read_file(filename):
    return np.array(list(map(lambda x:float(x.strip('\n')),(open(filename,'r').readlines()))))
if __name__ =='__main__':
    try:
        assert(len(s.argv)>=2)
    except:
        print("Please insert file name")
        print("May be specified is reside in your system")
    x=read_file(s.argv[1])
    plot_it(x,len(x))
