def make_dict(lskey,lsval):
    tempdict={}
    if len(lskey) <= len(lsval):
        for count in range(0,len(lskey)):
            tempdict[lskey[count]]=lsval[count]
    return tempdict
