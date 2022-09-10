import Funcs as f
X = []


fil= open('data10.txt',mode='r')
arr=fil.read().split(',')
for i in arr:
    X.append(int(i))



array=f.Sort10(X)
print(array)