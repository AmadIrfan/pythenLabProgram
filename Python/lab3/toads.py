import random


def getPopulation(n):    
    array=[]
    for i in range(num):
        array.append(bool(random.randint(0, 1)))
    random.shuffle(array)
    return array

def TruthFulToadsA(population):
    lst=[]
    for i in range(len(population)):
        if(population[i]==1):
            population[i]="Trustworthy"
        else:
            population[i]="Tricky"
        
    for i in range(len(population)):
        if(population[i] == "Trustworthy"):
            lst.append(i)
    return lst




def TruthFulToadsB(population):
    lst1=[]
    arr=[]
    for i in range(len(population)//2):
        lst1.append(random.randint(1,1))
    for j in range(len(population)//2):
        lst1.append(random.randint(0,1))
    random.shuffle(lst1)
    for m in range(len(population)):
        if(population[m]==1):
            arr.append(lst1[i])
        else:
            ran=random.random()
            if(ran<0.5):
                arr.append(1)
            else:
                arr.append(0)
    lst2=[]
    for m in range(len(arr)):
        if(arr[m] == 1):
            lst2.append(m)
    
    return lst2
            
                        
num=int(input("Enter population : "))
population=getPopulation(num)
pop=TruthFulToadsA(population)
pop1=TruthFulToadsB(population)
print('Tode A say {} speak true'.format(pop))
print('Tode B say {} speak true'.format(pop1))