# arr=["Amad","Amna"]

# fil=open(file="text.txt", mode="w")
# for i in arr:
#     fil.writelines(i + ',')

file1=open(file="text.txt",mode="r")

line=file1.read()
name=[]

print(line)
arr1=line.split(',')
for i in arr1:
    name.append(i)
print(name)