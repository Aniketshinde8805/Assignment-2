
class Emp():
	def set_basic_details(self,name,dept,sal):
		self.name=name
		self.dept=dept
		self.sal=sal
	def display_basic_details(self):
		print("Name:",self.name)
		print("Department:",self.dept)
		print("Salary:",self.sal)

	def set_personal_details(self,age,group,city,state):
		self.age=age
		self.group=group
		self.city=city
		self.state=state

	def display_personal_details(self):
		print("Age:{} \nBloodGroup:{} \nCity:{} \nState:{}".format(self.age,self.group,self.city,self.state))

	def display_all(self):
		print("Name:",self.name)
		print("Department:",self.dept)
		print("Salary:",self.sal)
		print("Age:{} \nBloodGroup:{} \nCity:{} \nState:{}".format(self.age,self.group,self.city,self.state))

