import matplotlib.pyplot as plt
import numpy as np
import sys as s

def generate_random_lcg(m,a,c,zi):
    list1=[]
    ui = []
    z1=((a*zi)+c)//m
    while(z1 not in list1):
        list1.append(z1)
        ui.append(z1/m)
        zi=z1
        z1=((a*zi)+c)%m
    print(ui,list1)
    return ui
def plot_it(x):
    y = x[1:]+[x[0]]
    plt.scatter(x,y,marker='o')
    plt.show()

def find_variance(x):
    return np.var((np.array(x)))

if __name__ =='__main__':
    try:
        assert(len(z.argv())==4)
    except:
        print("Please enter valid number of argument")
    x = generate_random_lcg(float(s.argv[1]),float(s.argv[2]),float(s.argv[3]),float(s.argv[4]))
    plot_it(x)
    print(find_variance(x))
