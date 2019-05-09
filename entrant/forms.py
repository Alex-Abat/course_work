from django import forms
from entrant.models import Anketa, Special

class AnketaForm(forms.Form):
	fio = forms.CharField(max_length=100, label='ФИО')
	date = forms.CharField(max_length=10, label='Дата рождения')
	sr_obr = forms.CharField(max_length=20, label='Оконченное среднее учебное заведение')
	date_sr_obr = forms.CharField(max_length=10, label='Дата окончания учебного заведения')
	medal = forms.CharField(max_length=20, label='Hаличие красного диплома или золотой/серебряной медали')
	address = forms.CharField(max_length=30, label='Адрес')
	spec = forms.ModelChoiceField(queryset=Special.objects.order_by('-name'), label='Специальность')
	def save(self):
		anketa = Anketa(**self.cleaned_data)
		anketa.save()
		return anketa

class SpecialForm(forms.Form):
	name = forms.CharField(max_length=20)

	def save(self):
		special = Special(**self.cleaned_data)
		special.save()
		return special