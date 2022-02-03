# 6.	Write a python program to convert the below two lists to dictionary
#    	Inputs:
#     list1 = [15, 16, 20, 35, 25, 45, 41]
#     range = ['0-10','10-20','20-30','30-40','40-50']
#     Expected output: [('0-10', []), ('10-20', [15,16]), ('20-30', [20, 25]), ('30-40', [35]), ('40-50', [41,45])]



def dz(l1,l2):
    d1=dict()
    for i in l2:
        tt=list(map(int,i.split("-")))
        d1[i]=[value for value in l1 if value in range(tt[0],tt[-1])]
    print(d1)





dz([15, 16, 20, 35, 25, 45, 41],['0-10','10-20','20-30','30-40','40-50'])
