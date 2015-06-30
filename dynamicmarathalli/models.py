from django.db import models

class Division(models.Model):
	name = models.CharField(max_length=30)

class Chapter(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return "Chapter: %s"%self.name

class District(models.Model):
	name = models.CharField(max_length=30)	
	chapter = models.ForeignKey(Chapter)

class Person(models.Model):
	name = models.CharField(max_length = 40)
	email = models.EmailField(blank = True)
	division = models.ForeignKey(Division)
	district = models.ForeignKey(District)

class DaimokuChanted(models.Model):
	person = models.ForeignKey(Person)
	start_date = models.DateField('period start')
	end_date = models.DateField('period end')
	hours = models.IntegerField()

	
	

