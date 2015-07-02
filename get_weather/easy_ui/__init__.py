from __future__ import print_function
class YesNo:
	def __init__(self, n):
		n.upper()
		if n=="y" or n=="yes":
			self.replace=True
		elif n=="n" or n=="no":
			self.replace=False
		else:
			raise ValueError("Bad option")



class Ui:
	def initialize_menu(self):
		print("{options:^40}\n\n".format(options="options:"))
		print("{index:<10}{item:>10}".format(item="exit", index=0))

		for index, item in enumerate(self.funcDict.keys()):
			print("{index:<10}{item:>10}".format(item=item, index=index+1))
		self.max=len(list(self.funcDict.keys()))

	def getraw_input(self):
		d=True
		while d:
			try:
				self.choice=int(raw_input("enter your choice"))
				if self.choice>self.max:
					raise ValueError("Value too large")
				break
			except ValueError as e:
				if str(e)=="Value too large":
					print("item not in the menu.")
				else:
					print("That was a bad option you gave me.\nEnter one of the numbers above.")
				self.initialize_menu()
		if 0 == self.choice:
			print("Good Bye, Exiting program.")
			exit()

	def callIt(self):
		option=list(self.funcDict.values())[self.choice-1] # get the 3-toople.
		#an option is a toople of the function, and then a toople of 2-tooples with items in the form of (type, prompt)  
		args=[]
		for theType, toPrint in option[1:]:
			while True:
				print("{:^20}".format(toPrint))
				#types provided by the class to make life easier.
				#This is a map of genaric types, or miscellaneous types, and their respective built-in helper. 
				#To get at the actual type that we should have, a .replace variable should be provided with what we want to actually give the function. See the YesNo typeclass for an example.
				#In the future I will allow the user to add types here, but that isn't currently implemented.
				inMap = False # if it is in the map we set this to True.
				types = {
					bool : YesNo,
				}
				if theType in types:
					inMap = True
					theOldType = theType
					theType = types[theOldType]
				try:
					that = theType(raw_input())
					if inMap:
						args.append(that.replace)
					else:
						args.append(that)
					break
				except ValueError:
					print("{:^20}".format("bad option? Try entering that again."))
		option[0](*args) #call it with our just built list of arguements.


	def __init__(self, funcDict):
		self.funcDict=funcDict
		while True:
			try:
				self.initialize_menu()
				self.getraw_input()
				self.callIt() #choice is implicit, passed in on self.choice.
			except KeyboardInterrupt:
				print("Do you really wish to exit? y/n")
				while True:
					try:
						d=YesNo(raw_input(""))
						break
					except ValueError:
						print("Bad option.")
				if d.replace:
					exit()
				else:
					continue










