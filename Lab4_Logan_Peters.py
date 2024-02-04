upBound = int(input())
propDiv = 0


pNum = 0
aNum = 0
dNum = 0

for num in range(1, upBound+1, 1):
    for i in range(1, num-1, 1):
        if(num%i==0):
            propDiv = propDiv + i
    if(propDiv == num):
        pNum = pNum + 1
    if(num<propDiv):
        aNum = aNum + 1
    if(num>propDiv):
        dNum = dNum + 1
    propDiv = 0


print (dNum, 'deficient numbers')
print (pNum, 'perfect numbers')
print (aNum, 'abundant numbers')