def find_char(strlist, char):

    templist=[]
    for element in strlist:

        if isinstance(element,basestring) and element.count(char)>0:

            templist.append(element)

    return templist
