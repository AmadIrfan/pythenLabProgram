Input=[[1,4],[2,5],[7,9],[9,10],[6,10]]



def friendSlower(Input):
    AllPairs=[]
    for i in range(len(Input)):
        for j in range(i,len(Input)):
            if i!=j:
                Pair=[]
                if   Input[j][0]<=Input[i][0] and Input[j][1]>=Input[i][0] or  Input[i][1]<=Input[j][1] and Input[i][1]>=Input[j][0]:
                    Pair.append(i+1)
                    Pair.append(j+1)
                    AllPairs.append(Pair)


    return tuple(map(tuple,AllPairs))   
pair=friendSlower(Input)          
print(pair)