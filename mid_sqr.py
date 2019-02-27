import numpy as np
import sys as s

def generate_random(zi):
    i =0
    z1_i = int(str(np.square(zi))[2:6])
    while(zi!=z1_i and z1_i!=0):
        print(z1_i,zi,np.square(zi))
        zi=z1_i
        st1=str(np.square(zi))
        if(len(st1)/4<2):
            z1_i = int(st1[1:5])
        else:
            z1_i = int(st1[2:6])
    return True

if __name__ =='__main__':
    generate_random(int(s.argv[1]))
