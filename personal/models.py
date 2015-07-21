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
    along with my personal website.  If not, see <http://www.gnu.org/licenses/>."""
from django.db import models

# Create your models here.
class Software_list(models.Model):
    name=models.CharField(max_length=20)
    description = models.TextField()
    source_code_download =models.URLField(blank=True)
    
    def truncated_discription(self):
        index=50
        length = len(self.description)
        while index < length:
            if self.description[index] != ' ':
                index+=1
            else:
                break
        st=self.description[:index]
        if index < len(self.description):
            st+="..."
        return st
    
    def get_latest_version(self):
        versions=sorted(list(self.version_set.all()))
        return versions[-1]
    get_latest_version.short_description= "Latest version:"
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name ="software"
        verbose_name_plural = "pieces of software"

class Version(models.Model):
    software=models.ForeignKey('Software_list')
    date_released=models.DateField()
    major_version_number = models.PositiveIntegerField()
    minor_version_number = models.PositiveIntegerField()
    sub_version_number = models.PositiveIntegerField()
    stable_release = models.BooleanField(default=True)
    download=models.URLField()
    
    def __str__(self):
        return "{major}.{minor}.{sub_version}{stable}".format(
            major = self.major_version_number,
            minor = self.minor_version_number,
            sub_version = self.sub_version_number,
            stable = "" if self.stable_release else ".dev"
        )
    
    def __lt__(self,other):
        a=self.major_version_number 
        a_other = other.major_version_number
        b=self.minor_version_number
        b_other = other.minor_version_number
        c=self.sub_version_number 
        c_other = other.sub_version_number
        if a < a_other:
            return True
        elif a > a_other:
            return False
        if b < b_other:
            return True
        elif b > b_other:
            return False
        if c < c_other:
            return True
        elif c > c_other:
            return False
        #Well, they are the same version number, but checking to see if one is stable while the other is dev.
        if self.stable_release < other.stable_release:
            return True
        return False


