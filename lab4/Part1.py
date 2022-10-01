
import matplotlib.pyplot as plt
import pandas as pd


def collectSameData(list1,list2):
    dateList=[]
    sumList=[]
    for i in range(len(list1)):
        if(list1[i]==0):
            continue
        else:
            date=list1[i]
            sum=0
            for j in range(i,len(list1)):
                if(date==list1[j]):
                    sum=sum+list2[j]
                    list1[i]=0
                    list1[j]=0
            dateList.append(date)
            sumList.append(sum)
    return  dateList,sumList



df=pd.read_csv('dailySteps_merged.csv')
list1=df['ActivityDay'].values.tolist()
list2=df['StepTotal'].values.tolist()
dateList,stepList=collectSameData(list1, list2)
plt.plot(dateList,stepList,color='green' )
plt.title('Daily Steps')
plt.xlabel('steps')
plt.ylabel('Date')
plt.xticks(rotation=90)
plt.show()



df=pd.read_csv('dailyActivity_merged.csv')
list3=df['ActivityDate'].values.tolist()
list4=df['TotalDistance'].values.tolist()
dateList,stepList=collectSameData(list3, list4)
plt.bar(dateList,stepList,width=1,color=['red','black'])
plt.title('Daily Steps ')
plt.xlabel('steps')
plt.ylabel('Date')
plt.xticks(rotation=90)
plt.show()




df=pd.read_csv('sleepDay_merged.csv')
list1=df['SleepDay'].values.tolist()
list2=df["TotalTimeInBed"].values.tolist()
dateList,bedList=collectSameData(list1,list2)
plt.scatter(dateList,bedList)
plt.ylabel(' total time in bed (s)')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.show()



df=pd.read_csv('hourlySteps_merged.csv')
list1=df['ActivityHour'].values.tolist()
list2=df["StepTotal"].values.tolist()
hoursList,stepsList=collectSameData(list1, list2)

df=pd.DataFrame(hoursList)
df1=pd.DataFrame(stepsList)


print(df)
print(df1)


plt.pie(stepsList)
plt.ylabel(' total time in bed (s)')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.show()

