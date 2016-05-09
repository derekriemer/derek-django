import json
from collections import OrderedDict
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from tipOfTheDay.forms import TipForm, FileForm
from tipOfTheDay.models import Tip

TIP_NAME_TO_NUM = {
	"beginner" : 1,
	"intermediate" : 2,
	"advanced" : 4,
}

def addData(file):
	info =  json.load(file, object_pairs_hook = OrderedDict)
	for title, dict in info["tips"].items():
		tip = Tip()
		tip.title = title
		tip.text = dict["description"]
		tip.level = 0
		for i in dict["level"]:
			tip.level |= TIP_NAME_TO_NUM[i]
		tip.save()
		

@login_required
def index(request):
	tips = Tip.objects.all()
	context = {"tips": tips}
	return render(request, 'tipOfTheDay/index.htm', context)

@login_required
def getJSON(request):
	context = {}
	jsonObj = OrderedDict([
		("type" , "global"),
		("appname" , None),
	])
	tips = OrderedDict()
	for tip in Tip.objects.all():
		tips[tip.title] = {
			"description" : tip.text,
			"level" : tip.getLevelList()
		}
	jsonObj["tips"] = tips
	return HttpResponse(json.dumps(jsonObj, separators = (",", " : "), indent=4), content_type='application/json')

@login_required
def putJson(request):
	context = {"send_to_url" : "tipOfTheDay:fu", "other_attrs" : 'enctype="multipart/form-data"'}
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			addData(request.FILES[u"file"])
			return HttpResponseRedirect('/tipOfTheDay/')
		else:
			context.update({'form': form, 'errors': True})
	else:
		form = FileForm()
		context.update({"form" : form})
	return render(request, 'tipOfTheDay/tip.htm', context)

@login_required
def tip(request):
	context = {"send_to_url" : "tipOfTheDay:tip", "other_attrs" : ""}
	if request.method == 'POST':
		form = TipForm(request.POST)
		if form.is_valid():
			pk = request.POST["pk"]
			if pk != "0":
				tip = Tip.objects.get(pk=pk)
				tip.title = form.cleaned_data["title"]
				tip.level = form.cleaned_data["level"]
				tip.text = form.cleaned_data["text"]
				tip.save()
			else:
				form.save()
			return HttpResponseRedirect('/tipOfTheDay/')
		else:
			context.update({'form': form, 'errors': True, 'pk' : int(request.POST["pk"])})
	else:
		try:
			pk = request.GET['pk']
			tip = Tip.objects.get(pk = pk)
			form = TipForm(instance = tip)
			context["pk"] = pk
			context["title"] = tip.title
			context["form"] = form
		except (KeyError, ObjectDoesNotExist):
			form = TipForm()
			context.update({"form" : form, "pk" : 0})
	return render(request, 'tipOfTheDay/tip.htm', context)

@login_required
def delete(request):
	print "hello"
	if request.method == "POST":
		try:
			pk = request.POST["pk"]
			print pk
		except KeyError:
			return Http404
		try:
			pk = Tip.objects.get(pk=pk)
			print pk
			pk.delete()
			return HttpResponseRedirect("/tipOfTheDay/")
		except ObjectDoesNotExist:
			raise Http404
	else:
		raise Http404
	return self.index(request)