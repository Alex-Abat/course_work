from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from entrant.forms import AnketaForm, ExamForm
from entrant.models import Anketa, Special, Exam

def index(request):#главная страница
	return render(request, 'index.html')

def add_anketa(request):#добавление анкеты
	if request.method == "POST":
		form = AnketaForm(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponse("</p>Анкета была успешно отправлена!</p><br><a href='/'>Вернутся обратно</a>")
	else:
		form = AnketaForm()
	return render(request, 'add.html', {'form':form,
		                                'name': 'Добавление анкеты'})

def show_all_anketa(request):#просмотр всех анкет
	ank = Anketa.objects.all()
	ex = Exam.objects.all()
	return render(request, "show_all_anketa.html", {'ankets':ank,
	                                                'ex': ex})

def exam(request):#добавление результата экзамена
	if request.method == "POST":
		form = ExamForm(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponse("</p>Результат экзамена был успешно отправлена!</p><br><a href='/exam/'>Вернутся обратно</a>")
	else:
		form = ExamForm()
	return render(request, 'add.html', {'form' :form,
			                            'name' : 'Добавление результата экзамена'})
