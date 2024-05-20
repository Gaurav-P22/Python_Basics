lis1=[1,2,3]
list2=[1,2,2,1]

copy_list=list2.copy()
copy_list.reverse()
if copy_list==list2:
    print("Palindrome")
else:
    print("Not Palindrome")