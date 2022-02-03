# 7	Write a Python function that that prints out the first n rows of Pascal's triangle.
# 	Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
# 	Ex = if input n = 2
# 			output 
# 			1
# 			1,1

# 	Ex = if input n = 4
# 			output 
# 			1
# 			1,1
# 			1,2,1
# 			1,3,3,1

# 	Ex = if input n = 6
# 		output 
# 			1
# 			1,1
# 			1,2,1
# 			1,3,3,1
# 			1,4,6,4,1
# 			1,5,10,10,5,1


def pascal():
	n=int(input("Enter the number"))

	l1=[]
	for i in range(n):
		l2=[]
		for j in range(i+1):
			if j==0 or j==i:             				#condition for 1's  position
				l2.append(1)
			else:                         				# else condition for centeral elements of row of triangle
				l2.append(l1[i-1][j-1] + l1[i-1][j])   # calculating center elements triangle's row
		l1.append(l2)                                  #nesting l2[] into l1[]

	for i in l1:                 #printing nested list l1[] in triangle pattern
		for j in i:
			print(j,end=",")
		print("")

pascal()