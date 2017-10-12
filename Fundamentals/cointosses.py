import random
def coinflip(flips):
    count=1
    heads=0
    tails=0
    while count <= flips:
        temp=random.randint(0,1)
        if temp==0:
            tempstr="tails"
            tails+=1
        else:
            tempstr="heads"
            heads+=1
        print "Attempt #"+str(count)+" Throwing a coin... It's "+tempstr+"! So far "+str(heads)+" heads and "+str(tails)+" tails."
        count+=1
coinflip(5000)
