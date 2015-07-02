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
class ApiKey(models.Model):
    name=models.CharField(max_length=20)
    api_key=models.CharField(max_length=2048)
    
    def __str__(self):
        return self.name