def filter(input):
#integer filter
    if isinstance(input, int)==True:
        if input >= 100:
            print "That's a big number!"
        else:
            print "That's a small number."
#string filter
    if isinstance(input, basestring)==True:
        if len(input)>=50:
            print "Long sentence."
        else:
            print "Short sentence."
#list filter
    if isinstance(input, list)==True:
        if len(input)>=10:
            print "Big list!"
        else:
            print "Short list"
exptestlist=[]
exptestlist.append(45)
exptestlist.append(100)
exptestlist.append(455)
exptestlist.append(0)
exptestlist.append(23)
exptestlist.append("Rubber baby buggy bumpers")
exptestlist.append("Experience is simply the name we give our mistakes")
exptestlist.append("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
exptestlist.append("")
exptestlist.append([1,7,4,21])
exptestlist.append([3,5,7,34,3,2,113,65,8,89])
exptestlist.append([4,34,22,68,9,13,3,5,7,9,2,12,45,923])
exptestlist.append([])
exptestlist.append(['name','address','phone number','social security number'])
for element in exptestlist:
    filter(element)
