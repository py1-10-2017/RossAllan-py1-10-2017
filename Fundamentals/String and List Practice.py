#Find and Replace
thanksday="It's thanksgiving day. It's my birthday, too!"
print thanksday.find("day")
thanksmonth=thanksday.replace("day","month")
#Min and Max
def min_max(nums):
    print min(nums)
    print max(nums)
#First and Last
def first_last(fal):
    firstlast=fal[0]+fal[len(fal)-1]
    print firstlast
#New List
def new_list(start):
    tempfull=sorted(start)
    tempfr=tempfull[0:len(tempfull)/2]
    tempback=tempfull[(len(tempfull)/2):len(tempfull)]
    tempback.insert(0,tempfr)
    return tempback
