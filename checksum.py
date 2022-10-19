polynomialCode = input("다항코드를 입력해주세요: ")
data = input("데이터를 입력해주세요: ")

polynomialCodeX=polynomialCode.split("+")

numList=[]

for element in polynomialCodeX:
    if element == "x":
        numList.append(1)
    elif element == "1":
        numList.append(0)
    else:
        list(element)
        for i in element:
            if i not in ['x','X', '^']:
                numList.append(int(i))

maxIndex=numList[0]

dataLen = len(data)
dataToAdd = ""

for i in range(0,maxIndex):
    dataToAdd+="0"

addedData = data+dataToAdd

replaceWithZero = "0"*(maxIndex+1)

replaceWithZeroAndOne = list(replaceWithZero)
for i in numList:
    replaceWithZeroAndOne[i]="1"
replaceWithZeroAndOne.reverse()

addedDataList = list(addedData)
replaceWithZeroList = list(replaceWithZero)


# maxIndex 다항식의 최고차항
# 1일때 비교할거는 replaceWithZeroAndOne[100101]
# 0일때 비교할거는 replaceWithZerolist[000000]
# 비교할것은 addedDatalist[10110100100000]
# dataLen 비교할 횟수


for i in range(0,dataLen):
    if addedDataList[i] == "1":
        for j in range(0, maxIndex+1):
            if addedDataList[i+j] == replaceWithZeroAndOne[j]:
                addedDataList[i+j]="0"
            else:
                addedDataList[i+j]="1"
    elif addedDataList[i] == "0":
        for j in range(0,maxIndex+1):
            if addedDataList[i+j] == replaceWithZeroList[j]:
                addedDataList[i+j]="0"
            else:
                addedDataList[i+j]="1"

def listToString(str_list):
    returnResult = ""
    for s in str_list:
        returnResult += s + ""
    return returnResult.strip()

result=listToString(addedDataList)
resultNum=result[-maxIndex:]


actualTransmittedData=data+resultNum
print("실제 전송 데이터는: "+actualTransmittedData)
