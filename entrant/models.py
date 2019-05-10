from django.db import models

class Special(models.Model):#таблица со специальностями
	name = models.CharField(max_length=20)#название
	def __str__(self):
		return self.name

class Disc(models.Model):#таблица с дисциплинами
	name = models.CharField(max_length=20)#название
	def __str__(self):
		return self.name

class Anketa(models.Model): #таблица с анкетами аббитуриентов
	fio = models.CharField(max_length=100)#ФИО
	date = models.DateField()#дата рождения
	sr_obr = models.CharField(max_length=20)#Среднее образование
	date_sr_obr = models.DateField()#дата окончания учебного заведения
	medal = models.CharField(max_length=20)#наличие медали
	address = models.CharField(max_length=30)#адрес
	spec = models.ForeignKey(Special, on_delete=models.SET_NULL, null=True, default=True, blank=True)# связь один-многие с таблицей специальностей
	def __str__(self):
		return self.fio

class Exam(models.Model):#таблица с результатами экзаменов
	entrant = models.ForeignKey(Anketa,on_delete=models.SET_NULL, null=True, default=True, blank=True)#связь один-многие с таблицей анкет
	disc = models.ForeignKey(Disc, on_delete=models.SET_NULL, null=True, default=True, blank=True)#связь один-многие с таблицей дисциплин
	ball = models.IntegerField(default=0)#оценка