# 3	Write a function that takes a list and returns a new list that contains 
# 	all the elements of the first list minus duplicates and other list with duplicates

# 	Ex - [1, 2, 3, 4, 3, 2, 1 ,5]
# 		 unique - [1, 2, 3, 4, 5]
# 		 duplicate - [1, 2, 3]




def list_fun2(l1):
	l2=list(set(l1))  	 #unique elements
	l3=[]
	for x in l2:         # creating duplicate elements  list
		if l1.count(x)>1:
			l3.append(x) 
	return l2,l3

print(list_fun2([1,2,3,4,3,2,1,5]))