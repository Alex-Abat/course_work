from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from entrant.forms import AnketaForm, ExamForm, SpecForm, DiscForm
from entrant.models import Anketa, Special, Exam, Disc

def index(request):#главная страница
	return render(request, 'index.html')

def add_anketa(request):#добавление анкеты
	if request.method == "POST":
		form = AnketaForm(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponse("</p>Анкета была успешно отправлена!</p><br><a href='/anketa'>Вернутся обратно</a>")
	else:
		form = AnketaForm()
	return render(request, 'add.html', {'form':form,
		                                'name': 'Создание анкеты'})
def add_disc(request):
	if request.method == "POST":
		form = DiscForm(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponse("</p>Специализация была успешно добавленна!</p><br><a href='/disc/'>Вернутся обратно</a>")
	else:
		form = DiscForm()
	return render(request, 'add_and_show.html', {'form':form,
		                                'name': 'Дисциплины',
		                                'list': Disc.objects.all()})

def add_spec(request):
	if request.method == "POST":
		form = SpecForm(request.POST)
		if form.is_valid():
			post = form.save()
			return HttpResponse("</p>Дисциплина была успешно добавленна!</p><a href='/spec/'>Вернутся обратно</a>")
	else:
		form = SpecForm()
	return render(request, 'add_and_show.html', {'form':form,
		                                'name': 'Специальности',
		                                'list': Special.objects.all()})

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
