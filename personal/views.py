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
    along with my personal website.  If not, see <http://www.gnu.org/licenses/>."""
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.core.mail import EmailMessage
from .forms import *
from django.conf import settings
TO = settings.EMAIL_ADDRESS_TO
#helper functions.
def getContext():
    return {
        "MENU_FILE" : "personal/menu.htm"
    }

#views
def index(request):
    context=getContext()
    return render(request, 'personal/index.htm', context)

def bio(request):
    context=getContext()
    return render(request, 'personal/bio.htm', context)

def contact(request):
    context=getContext()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            message = EmailMessage()
            message.subject = "[{} via website]".format(form.cleaned_data["your_name"])+form.cleaned_data["subject"]
            message.reply_to = [form.cleaned_data["sender"]]
            message.to=[TO]
            message.body = form.cleaned_data["message"]
            if form.cleaned_data["copy_myself"]:
                message.cc=[form.cleaned_data["sender"]]
            message.send()
            return HttpResponseRedirect('/personal/thanks/')
        else:
        
            context.update({'form': form, "errors": True})
            return render(request, 'personal/contact.htm', context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
        context.update({'form': form})
    return render(request, 'personal/contact.htm', context)

def thanks(request):
    context=getContext()
    return render(request, 'personal/thanks.htm', context)

def software(request):
    context=getContext()
    apps = Software.objects.all()
    context['apps'] = apps
    return render(request, 'personal/software.htm', context)