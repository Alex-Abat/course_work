from django.shortcuts import render
from django.http import HttpResponse
from entrant.forms import AnketaForm, SpecialForm 
from entrant.models import Anketa, Special

def index(request):
	return render(request, 'index.html')

def add_anketa(request):
	if request.method == "POST":
		form = AnketaForm(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponse("</p>Анкета была успешно отправлена!</p><a href='/'>На главную</a>")
	else:
		form = AnketaForm()
	return render(request, 'add_anketa.html', {'form':form,})

def add_spec(request):
	if request.method == "POST":
		form = SpecialForm(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponse("</p>Анкета была успешно отправлена!</p> <a href='/add_spec'>На главную</a>")
	else:
		form = SpecialForm()
	return render(request, 'add_spec.html', {'form':form,})

def show_all_anketa(request):
	ank = Anketa.objects.all()
	return render(request, "show_all_anketa.html", {'ankets':ank,})