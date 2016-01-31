"""This file Copyright (C) Derek Riemer, 2016
	This file is part of my personal website.

	my personal website is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	The back end code of my personal website is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with my personal website.  If not, see <http://www.gnu.org/licenses/>."""
from django.contrib import admin
from .models import Software_list, Version

# Register your models here.
class VersionInline(admin.TabularInline):
    fields = [
        'major_version_number',
        'minor_version_number',
        'sub_version_number',
        'stable_release',
        'date_released',
        'download',
    ]
    model = Version
    extra = 1
    show_change_link=True

class Software_list_admin(admin.ModelAdmin):
    inlines = [VersionInline]
    list_display=["name", "get_latest_version", "truncated_discription"]

admin.site.register(Software_list, Software_list_admin)