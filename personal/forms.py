"""This file Copyright (C) Derek Riemer, 2016
	This file is part of my personal website.

	my personal website is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	The code of my personal website is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with my personal website.  If not, see <http://www.gnu.org/licenses/>.
	Note that this code was modifyed off of the code on https://docs.djangoproject.com/en/1.8/topics/forms/
	"""
from django import forms
from django.core.exceptions import ValidationError
#helper functions.

def obfiscate(value):
    """ Obfiscates a given string by replacing it with the html numeric values of each of the characters. This helps to midagate some spam bots probably, but it isn't perfect, and not as good as a captcha. An example of this is like replacing space with &#32;
    """
    return "".join(["&#"+str(int(ord(i)))+";" for i in value])

def validate_checked(value):
    if value != False:
        raise ValidationError("Please uncheck the box.")

class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=60)
    sender = forms.EmailField(label="Your email")
    subject = forms.CharField(max_length=60)
    message = forms.CharField(widget=forms.Textarea)
    copy_myself = forms.BooleanField(required=False, initial=True, )
    i_am_a_robot = forms.BooleanField(validators=[validate_checked], required=False, label="Read the instructions about robots.", help_text=obfiscate("I hereby declare myself a member of the human species, and I am not a computer designed for the purpose of spamming innocent humans. I promise that my intentions are without evil, and that I am not a robot, spam bot, or any other form of of non-human life that wishes to spam legitiment human intentions. As a human, I prowdly will uncheck this box. I understand that if I fail to uncheck the box above, the email will simply not go through."), initial=True) #That will help to ensure that humans are the only thing submitting the form.
