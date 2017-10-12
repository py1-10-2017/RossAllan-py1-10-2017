def randgrades():
    import random
    score=random.randint(0,40)
    tempstring="Score: "+str(100-score)
    if score <= 10:
        tempstring+="; Your grade is A"
    elif score <=20:
        tempstring+="; Your grade is B"
    elif score <=30:
        tempstring+="; Your grade is C"
    elif score <=40:
        tempstring+="; Your grade is D"
    print tempstring
randgrades()
