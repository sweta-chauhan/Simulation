import matplotlib.pyplot as plt
import numpy as np
import sys as s

def generate_random(zi):
    i =0
    list1 =[]
    z1_i = int(str(np.square(zi))[2:6])
    while(zi!=z1_i and z1_i!=0 and (z1_i not in list1)):
        list1.append(z1_i)
        print(z1_i,zi,np.square(zi))
        zi=z1_i
        st1=str(np.square(zi))
        l1=len(st1)
        if(l1/4<2):
            if(l1==5):
                z1_i = int(st1[0:4])
            else:
                z1_i = int(st1[1:5])
        else:
            z1_i = int(st1[2:6])
            
    return list1

def plot_it(x):
    y = x[1:]+[x[0]]
    plt.scatter(x,y,marker='o')
    plt.show()

def find_variance(x):
    return np.var((np.array(x)))

if __name__ =='__main__':
    x = generate_random(int(s.argv[1]))
    plot_it(x)
    print(find_variance(x))
