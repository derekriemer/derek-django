"""This file Copyright (C) Derek Riemer, 2015
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

def validate_checked(value):
    if value != False:
        raise ValidationError("Please uncheck the box.")

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=60)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label="From")
    copy_myself = forms.BooleanField(required=False, initial=True, )
    i_am_a_robot = forms.BooleanField(validators=[validate_checked], required=False, label="Read the instructions about robots.", help_text="&#73;&#32;&#104;&#101;&#97;&#114;&#98;&#121;&#32;&#127;&#100;&#101;&#99;&#108;&#97;&#114;&#101;&#32;&#109;&#121;&#115;&#101;&#108;&#102;&#32;&#97;&#32;&#109;&#101;&#109;&#98;&#101;&#114;&#32;&#111;&#102;&#32;&#116;&#104;&#101;&#32;&#104;&#117;&#109;&#97;&#110;&#32;&#115;&#112;&#101;&#99;&#105;&#101;&#115;&#44;&#32;&#97;&#110;&#100;&#32;&#73;&#32;&#97;&#109;&#32;&#110;&#111;&#116;&#32;&#97;&#32;&#99;&#111;&#109;&#112;&#117;&#116;&#101;&#114;&#32;&#100;&#101;&#115;&#105;&#103;&#110;&#101;&#100;&#32;&#102;&#111;&#114;&#32;&#116;&#104;&#101;&#32;&#112;&#117;&#114;&#112;&#111;&#115;&#101;&#32;&#111;&#102;&#32;&#115;&#112;&#97;&#109;&#109;&#105;&#110;&#103;&#32;&#105;&#110;&#110;&#111;&#99;&#101;&#110;&#116;&#32;&#104;&#117;&#109;&#97;&#110;&#115;&#46;&#32;&#73;&#32;&#112;&#114;&#111;&#109;&#105;&#115;&#101;&#32;&#116;&#104;&#97;&#116;&#32;&#109;&#121;&#32;&#105;&#110;&#116;&#101;&#110;&#116;&#105;&#111;&#110;&#115;&#32;&#97;&#114;&#101;&#32;&#119;&#105;&#116;&#104;&#111;&#117;&#116;&#32;&#101;&#118;&#105;&#108;&#44;&#32;&#97;&#110;&#100;&#32;&#116;&#104;&#97;&#116;&#32;&#73;&#32;&#97;&#109;&#32;&#110;&#111;&#116;&#32;&#97;&#32;&#114;&#111;&#98;&#111;&#116;&#44;&#32;&#115;&#112;&#97;&#109;&#32;&#98;&#111;&#116;&#44;&#32;&#111;&#114;&#32;&#97;&#110;&#121;&#32;&#111;&#116;&#104;&#101;&#114;&#32;&#102;&#111;&#114;&#109;&#32;&#111;&#102;&#32;&#127;&#111;&#102;&#32;&#110;&#111;&#110;&#45;&#104;&#117;&#109;&#97;&#110;&#32;&#108;&#105;&#102;&#101;&#32;&#116;&#104;&#97;&#116;&#32;&#119;&#105;&#115;&#104;&#101;&#115;&#32;&#116;&#111;&#32;&#115;&#112;&#97;&#109;&#32;&#108;&#101;&#103;&#105;&#116;&#105;&#109;&#101;&#110;&#116;&#32;&#104;&#117;&#109;&#97;&#110;&#32;&#105;&#110;&#116;&#101;&#110;&#116;&#105;&#111;&#110;&#115;&#46;&#32;&#65;&#115;&#32;&#97;&#32;&#104;&#117;&#109;&#97;&#110;&#44;&#32;&#73;&#32;&#112;&#114;&#111;&#119;&#100;&#108;&#121;&#32;&#119;&#105;&#108;&#108;&#32;&#117;&#110;&#99;&#104;&#101;&#99;&#107;&#32;&#116;&#104;&#105;&#115;&#32;&#98;&#111;&#120;&#46;&#32;&#73;&#32;&#117;&#110;&#100;&#101;&#114;&#115;&#116;&#97;&#110;&#100;&#32;&#116;&#104;&#97;&#116;&#32;&#105;&#102;&#32;&#73;&#32;&#102;&#97;&#105;&#108;&#32;&#116;&#111;&#32;&#117;&#110;&#99;&#104;&#101;&#99;&#107;&#32;&#116;&#104;&#101;&#32;&#98;&#111;&#120;&#32;&#97;&#98;&#111;&#118;&#101;&#44;&#32;&#116;&#104;&#101;&#32;&#101;&#109;&#97;&#105;&#108;&#32;&#119;&#105;&#108;&#108;&#32;&#115;&#105;&#109;&#112;&#108;&#121;&#32;&#110;&#111;&#116;&#32;&#103;&#111;&#32;&#116;&#104;&#114;&#111;&#117;&#103;&#104;&#46;", initial=True) #That will help to ensure that humans are the only thing submitting the form.
