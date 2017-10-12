def listcompare(lsone,lstwo):

    same=True
    if len(lsone)==len(lstwo):

        count=0
        while count<len(lsone):

            if lsone[count] != lstwo[count]:

                print "The lists are not the same."
                same=False
                break

            else:

                count+=1

    else:

        print "The lists are not the same."
        same=False

    if same==True:

        print "The lists are the same"
