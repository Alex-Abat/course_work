from django.db import models

class Special(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Disc(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Anketa(models.Model): # Анкета
	fio = models.CharField(max_length=100)
	date = models.CharField(max_length=10)
	sr_obr = models.CharField(max_length=20)
	date_sr_obr = models.CharField(max_length=10)
	medal = models.CharField(max_length=20)
	address = models.CharField(max_length=30)
	spec = models.ForeignKey(Special, on_delete=models.SET_NULL, null=True, default=True, blank=True)

class Exam(models.Model):
	entrant = models.ForeignKey(Anketa,on_delete=models.SET_NULL, null=True, default=True, blank=True)
	disc = models.ForeignKey(Disc, on_delete=models.SET_NULL, null=True, default=True, blank=True)
	ball = models.IntegerField(default=0)