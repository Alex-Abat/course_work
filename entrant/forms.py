from django import forms
from entrant.models import Anketa, Special, Disc, Exam
from django.forms.widgets import DateInput

class AnketaForm(forms.Form):#форма для добавления анкеты
	fio = forms.CharField(max_length=100, label='ФИО')
	date = forms.DateField( input_formats=('%d-%m-%Y',), widget=DateInput, label='Дата рождения(дд-мм-гггг)')
	sr_obr = forms.CharField(max_length=20, label='Оконченное среднее учебное заведение')
	date_sr_obr = forms.DateField(input_formats=('%d-%m-%Y',), widget=DateInput,label='Дата окончания учебного заведения(дд-мм-гггг)')
	medal = forms.CharField(max_length=20, label='Hаличие красного диплома или золотой/серебряной медали')
	address = forms.CharField(max_length=30, label='Адрес')
	spec = forms.ModelChoiceField(queryset=Special.objects.order_by('-name'), label='Специальность')
	
	def save(self):
		anketa = Anketa(**self.cleaned_data)
		anketa.save()
		return anketa

class ExamForm(forms.Form):#форма для добавления результата экзамена
	entrant = forms.ModelChoiceField(queryset=Anketa.objects.order_by('-fio'), label='ФИО аббитуриента')
	disc = forms.ModelChoiceField(queryset=Disc.objects.order_by('-name'), label='Дисциплина')
	ball = forms.IntegerField(label='Оценка')

	def save(self):
		a = Exam(**self.cleaned_data)
		a.save()
		return a