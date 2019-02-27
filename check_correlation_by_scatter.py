import matplotlib.pyplot as plt
import sys as s
import reader as r

def plot_it(x,size):
    y = x[1:]+[x[-1]]
    plt.scatter(x,y,marker='o')
    plt.show()

if __name__ =='__main__':
    try:
        assert(len(s.argv)>=2)
    except:
        print("Please insert file name")
        print("May be specified is reside in your system")
    x=r.read_file(s.argv[1])
    plot_it(x,len(x))