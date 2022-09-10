
import Funcs as f

X = []
fil=open('data4.txt',mode='r')
lines=fil.read()
arr=lines.split(',')

for i in arr:
    X.append(int(i))


array=f.Sort4(X)
print(array)
