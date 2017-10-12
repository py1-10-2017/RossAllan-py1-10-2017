#Multiples Part One
def multi1():
    for count in range(1,1000):
        if count%2==0:
            continue
        else:
            print count
#Multiples Part Two
def multi2():
    onemil=5
    while onemil <= 1000000:
        print onemil
        onemil+=5
#Sum List
def sum(sumlist):
    tempsum=0
    for element in sumlist:
        tempsum+=element
    print tempsum
sum([1,2,5,10,225,3])
#Average List
def average(averagelist):
    avgtempsum=0
    for element in averagelist:
        avgtempsum+=element
    avgtemp=avgtempsum/len(averagelist)
    print avgtemp
average([1,2,5,10,225,3])
