import csv


def read_csv(filename):
    with open(filename) as csvfile:
        readCSV = list(map(lambda x:float(x[0]),csv.reader(csvfile)))
    return readCSV

def read_csv_two_col(filename):
    fp = open(filename)
    chi_tab = {}
    readCSV = list(csv.reader(fp,delimiter=','))
    for _ in readCSV:
        chi_tab.update({int(_[0]):float(_[1])})
    return chi_tab
    

def read_file(filename):
    return list(map(lambda x:float(x.strip('\n')),(open(filename,'r').readlines())))


#print(read_csv_two_col('chi_square_table_with_05_significance.csv'))
