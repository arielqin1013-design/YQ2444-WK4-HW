for i in range(0,6):
    print(i) 

mylist = ['cat','dog','fish']




for x in mylist:
    print(x)


i = 0
while i < 6:
    i += 1
    print(i)



i = 0
while i < 6:
    print(i)
    i = i + 1
    

def MySum(a,b):
    value = a+b
    return(value)

MySum(3,5)

MySum(2,3)

a = [1,2,3]

a

a.reverse()

a

a = [3, 6, 4]

a.sort()


a

# Tuple

mytup = (1,2,3)
for x in mytup:
    print(x)




# Error:
mytup[0] = 10


a[2]

a = 3

a

b = 4

a == b

a = b

a

mylist = ['cat','dog','fish']
for i,x in enumerate(mylist): #枚举
    print(i,x)


mylist = ['cat','dog','fish']
mylist2 = ['lion','wolf','whale']
for x,y in zip(mylist,mylist2):
    print(x,y)


def WhoAmI():
    return('YQ2444')

WhoAmI()

a = 3

a

print(a)

def getBondPrice(y, face, couponRate, m, ppy=1):
    c = face * couponRate / ppy
    bondPrice = 0
    m = m * ppy
    y = y / ppy
    for i in range(1, m + 1):
        bondPrice = bondPrice + c / (1 + y) ** i 
    bondPrice += face / (1 + y) ** m
    return(bondPrice)

getBondPrice(0.03, 2000000, 0.04, 10)

getBondPrice(0.03, 2000000, 0.04, 10, 1)

getBondPrice(0.03, 2000000, 0.04, 10, 2)

def getBondDuration(y, face, couponRate, m, ppy = 1):
    price =  getBondPrice(y, face, couponRate, m, ppy)
    c = face * couponRate / ppy
    bondDuration = 0
    m = m * ppy
    y = y / ppy
    for i in range(1, m + 1):
        bondDuration += c / (1 + y) ** i / price * i
    bondDuration += face / (1 + y) ** m / price * m
    bondDuration = bondDuration / ppy
    return(bondDuration)


getBondDuration(0.03, 2000000, 0.04, 10)

getBondDuration(0.03, 2000000, 0.04, 10, 1)

getBondDuration(0.03, 2000000, 0.04, 10, 2) #8.42

def getBondPrice_E(face, couponRate, m, yc):
    c = face * couponRate
    bondPrice = 0
    for i,y in enumerate(yc):
        bondPrice += c / (1 + y) ** (i + 1)
    bondPrice += face / (1 + yc[-1]) ** m
    return(bondPrice)


mylist = ['cat','dog','fish']
for i,x in enumerate(mylist): 
    print(i,x)

a = [1,4,6,2,3,4,5,6,4,2,567,7]

a[-1]

getBondPrice_E(2000000, 0.04, 5, [0.01,0.015,0.02,0.025,0.03])

a = [1,4,6]
len(a)

a[len(a)-1]

def getBondPrice_E(face, couponRate, m, yc):
    c = face * couponRate
    bondPrice = 0
    n = len(yc)
    for i in range(0, n):
        bondPrice += c / (1 + yc[i]) ** (i + 1)
    bondPrice += face / (1 + yc[-1]) ** m
    return(bondPrice)

getBondPrice_E(2000000, 0.04, 5, [0.01,0.015,0.02,0.025,0.03])

mylist = ['cat','dog','fish']
mylist2 = ['lion','wolf','whale']
for x,y in zip(mylist,mylist2):
    print(x,y)

def getBondPrice_Z(face, couponRate, times, yc):
    c = face * couponRate
    bondPrice = 0
    n = len(times)
    for i in range(0, n):
        bondPrice += c / (1 + yc[i]) ** times[i]
    bondPrice += face / (1 + yc[-1]) ** times[-1]
    return(bondPrice)
    

getBondPrice_Z(2000000, 0.04, [1,1.5,3,4,7], [0.01,0.015,0.02,0.025,0.03])

def getBondPrice_Z(face, couponRate, times, yc):
    c = face * couponRate
    bondPrice = 0
    for i,y in zip(times, yc):
        bondPrice += c / (1 + y) ** i
    bondPrice += face / (1 + yc[-1]) ** times[-1]
    return(bondPrice)
    

getBondPrice_Z(2000000, 0.04, [1,1.5,3,4,7], [0.01,0.015,0.02,0.025,0.03])

def FizzBuzz(start, finish):
    outlist = []
    for i in range(start, finish + 1):
        if i % 3 == 0 and i % 5 == 0:
            outlist.append("fizzbuzz")
        elif i % 3 == 0:
            outlist.append("fizz")
        elif i % 5 == 0:
            outlist.append("buzz")
        else:
            outlist.append(str(i))
        
    return(outlist)

myEmptyList = []
for i in range(1,5):
    myEmptyList.append(i)
print(myEmptyList)

4 % 3

print(FizzBuzz(1,15))

print(FizzBuzz(106,129))



