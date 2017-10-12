def listanalysis(ltbd):
    strtemp=""
    sumtemp=0
    if isinstance(ltbd,list)==True:
        for element in ltbd:
            if isinstance(element,basestring)==True:
                strtemp+=element+" "
            elif isinstance(element,int)==True or isinstance(element,float)==True:
                sumtemp+=element
            else:
                continue
    if strtemp!="" and sumtemp!=0:
        print "The list you entered is of mixed type"
        print sumtemp
        print strtemp
    else:
        if strtemp!="":
            print "The list you entered is of string type"
            print strtemp
        if sumtemp!=0:
            print "The list you entered is of number type"
            print sumtemp
