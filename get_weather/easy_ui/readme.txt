How to use this.

Place the folder in your project.
Now, type 
import easy_ui

## dictionaries.

then you will create a dictionary of key-value pairs of keys being the menu items, the values being 3 tooples.

## The 3-tooples.

Each 3 toople is to have:

*Item 1 being the function
*item 2 being a toople of the functions types.
*Item 3 being a toople of what to prompt for each item.

## Example.


This will ask the user what they want for dinner.

                     dinner.py:
import easy_ui

def hotdog(numberOfHotdogs, chilly, cheese, musterd):
	message= "Your "
	if numberOfHotdogs < 1:
		print("um, Well, you might as well not have come into the hotdog stand! Hope you have a nice day.")
		return
	message=message+" chilly" if chilly else message
	if chilly and cheese:
		message+=", "
	elif chilly and musterd:
		message+=", and "
	else:
		message+=" "
	message=message+"cheese" if cheese else message
	if cheese and musterd:
		message+=", and "
	message=message+"musterd" if musterd else message
	if numberOfHotdogs > 1:
		message+=" hotdogs are "
	else:
		message+=" hotdog is "
	message+="ready to be devoured."
	print(message)

def icecream(chocolate):
	print("Okay. coming up.") if chocolate else print("dang. You don't want any chocolate? It's really good!!! Anyway, here's your icecream.")

ui = {
	"icecream" : (
		icecream, 
		(bool, "do you want some chocolate? y/n"),
	),
	"hotdog" : (
		hotdog,
		(int, "How many hot dogs would you like.",),
		(bool, "Do you want chilly?",),
		(bool, "Do you want cheese?",),
		(bool, "Do you want musterd?",)
	)
}
easy_ui.Ui(ui) #runs the ui asking the user what they want.