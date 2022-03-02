from django.db import models


class Publisher(models.Model):
	name = models.CharField(max_length=30)
	genre = models.CharField(max_length=30)	
	city = models.CharField(max_length=30)
	country = models.CharField(max_length=30)
	is_active = models.BooleanField()

	def __str__(self):
		return f'{self.id}. {self.name} ({self.country}, {self.city})'


class Autor(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	boigraphy = models.TextField()
	second_name = models.CharField(max_length=40)
	phone = models.CharField(max_length=16, blank=True)
	personal_page = models.URLField(blank=True)
	facebook = models.URLField(blank=True)
	twitter = models.CharField(max_length=50, blank=True)
	city = models.CharField(max_length=50, blank=True)
	country = models.CharField(max_length=50, blank=True)
	univercity = models.CharField(max_length=100, blank=True)
	birth_date = models.DateField(null=True, blank=True)

	def __str__(self):
		return f'{self.id}. {self.first_name} {self.last_name}'


class Book(models.Model):
	STATUS_CHOICES = [
		('d', 'Draft'),
		('r', 'Review'),
		('p', 'Published'),
	]
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Autor)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	publication_date = models.DateField()
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')