def yesno(n):
	n.upper()
	if n=="y" or n=="yes":
		return True
	elif n=="n" or n=="no":
		return False
	else:
		raise ValueError("Bad option")



class CreateUi:
	def initialize_menu(self):
		print("{options:^40}\n\n".format(options="options:"))
		print "{index:<10}{item:>10}".format(item="exit", index=0)

		for index, item in enumerate(self.funcDict.keys()):
			print "{index:<10}{item:>10}".format(item=item, index=index+1)
		self.max=len(self.funcDict.keys())

	def getInput(self):
		d=True
		while d:
			try:
				self.choice=int(raw_input("enter your choice"))
				if self.choice>self.max:
					raise(ValueError("value To Large."))
				break
			except ValueError as e:
				if e.message=="value To Large.":
					print "item not in the menu."
				else:
					print "That was a bad option you gave me.\nEnter one of the numbers above.."
				self.initialize_menu()
		if 0 == self.choice:
			exit()

	def callIt(self):
		option=self.funcDict.values()[self.choice-1] # get the first of the 3-toople.
		#an option is a 3-toople with item 0 as the func name, item 1 as the list of types, and option 2 as the list of things to print out for each individual item.
		args=[]
		for i, toPrint in enumerate(option[2]):
			while True:
				print "{:^20}".format(toPrint)
				itsType=option[1][i]
				#todo, extend typing system,
				try:
					args.append(itsType(raw_input()))
					break
				except ValueError:
					print "{:^20}".format("bad option? Try entering that again.")
		option[0](*args) #call it with our just built list of arguements.


	def __init__(self, funcDict):
		self.funcDict=funcDict
		while True:
			try:
				self.initialize_menu()
				self.getInput()
				self.callIt() #choice is implicit, passed in on self.choice.
			except KeyboardInterrupt:
				print "Do you really wish to exit? y/n"
				while True:
					try:
						d=yesno(raw_input(""))
						break
					except ValueError:
						print "Bad option."
				if d:
					exit()
				else:
					continue










