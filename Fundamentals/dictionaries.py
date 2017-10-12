my_info ={"name":"Ross","age":"21","country of birth":"United States","favorite language":"Ruby?"}
def dictionary(infodict):
    for key in infodict:
        print "My "+key+" is "+infodict[key]
dictionary(my_info)
