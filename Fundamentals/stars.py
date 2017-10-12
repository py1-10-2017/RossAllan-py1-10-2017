def draw_stars(starlist):
    for element in starlist:
        if isinstance(element,basestring):
            print element[0]*len(element)
        elif isinstance(element,int):
            print "*"*element
