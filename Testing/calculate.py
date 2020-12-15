import sys
import numpy as np

def calculate(data):
    # print(data)
    mean=0
    std = 0
    error=0.08
    # for i in range(0,len(data)):
    n = (np.std(data)*2.78/error)**2
    print(n)
    return n

if __name__ == "__main__":
    args = sys.argv
    name = args[1]
    count=0
with open(name) as file_in:
    data = np.array([])
    for line in file_in:
        p = line.strip()
        # print("k"+p+"k")
        count+=1
        # data=
        # data=np.append(data,float(line.strip()[:]))
        line=line.strip()
        # print(line[-2:len(line)])
        if line[-2:len(line)]=="ms":
            # print(data[-2:len(data)])
            data=np.append(data,float(line.strip()[:-2])/1000)
        else:
            # print(data[-2:len(data)])
            data=np.append(data,float(line.strip()[:-1]))
        line_number=calculate(data)
        if line_number<=count and count>1:
            print("Break reach",count)
            print(np.sum(data)/count)
            break    