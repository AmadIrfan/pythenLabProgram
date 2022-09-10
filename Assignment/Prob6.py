import Funcs as f

num=input('Enter a Number : ' )

number= f.SumIterative(int(num))
print ('Iterative Sum',number)
num=f.SumRecursive(number)
print('Recursive Sum',num)