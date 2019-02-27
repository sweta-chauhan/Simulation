
def read_file(filename):
    return list(map(lambda x:float(x.strip('\n')),(open(filename,'r').readlines())))

