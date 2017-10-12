#Odd/Even
def odd_even():
    for count in range(1,2001):
        if count%2==0:
            print "Number is",count,"This is an even number"
        else:
            print "Number is",count,"This is an odd number"
#Multiply
def multiply(multlist,multval):
    listemp=[]
    for element in multlist:
        listemp.append(element*multval)
    return listemp
#Hacker Challenge
def layermult(lsout):
    outtemplist=[]
    for element in lsout:
        intemplist=[]
        for count in range(0,element):
            intemplist.append(1)
        outtemplist.append(intemplist)
    return outtemplist
