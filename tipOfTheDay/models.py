from django.db import models
LEVEL_CHOICES = [
	(1, "beginner"),
	(2, "intermediate"),
	(4, "advanced"),
	(1|2, "beginner and intermediate"),
	(2|4, "intermediate and advanced"),
	(1|2|4, "Beginner, Intermediate, and Advanced"),
]

class Tip(models.Model):
	title = models.CharField(max_length=255, help_text = "The title of the tip. Keep it short.")
	level = models.PositiveSmallIntegerField(choices = LEVEL_CHOICES, help_text = "This is how familiar with windows the user should be when seeing this tip. Please note that this is <em> Not </em> how familiar the user is with NVDA.")
	text = models.TextField(help_text = "Write the tip here.")
	weight = models.PositiveSmallIntegerField(help_text = "the weight of the field. Tinkering with this causes this tip to appear earlier in the list. lowering the weight floats it to the top, while adding weight makes it sink down in the list.", 
		default = 0)
	
	class Meta:
		ordering = ['weight', 'pk']
	def getLevelList(self):
		levels = []
		if self.level & 1:
			levels.append("beginner")
		if self.level & 2:
			levels.append("intermediate")
		if self.level & 4:
			levels.append("advanced")
		return levels

	def getTruncatedText(self):
		index=50
		length = len(self.text)
		while index < length:
			if self.text[index] != ' ':
				index+=1
			else:
				break
		st=self.text[:index]
		if index < len(self.text):
			st+="..."
		return st
	