# 2   Create module for employe information having atleast three function 
# 	(example - basic details, personal details, print details, etc, you can add more)
# 	give module name as employee


from employee import Emp

aa=Emp()

aa.set_basic_details("Aniket","Engineering",25000)   

aa.set_personal_details(23,"O+ve","Pune","Maharashtra")

print('-----------------------Displaying Basic Details ---------------------------')
aa.display_basic_details()

print('-----------------Displaying Personal Details ---------------------------')
aa.display_personal_details()

print('--------------------Displaying Both Personal and Basic details ------------------------------')
aa.display_all()