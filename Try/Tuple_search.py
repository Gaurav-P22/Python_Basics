tup=(1,2,3,4,5,6,7,8)
idx=0
item=int(input("enter the no to search"))
flag=0
while idx<len(tup):
    if tup[idx]==item:
        flag=1
        break
    
    idx+=1
if flag==1:
    print("No Found at index",idx)
else:
    print("Not Found")  