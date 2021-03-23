from django.db import models
from django_countries.fields import CountryField


class Category(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	ordering = models.IntegerField(default=0)

	class Meta:
		verbose_name_plural='Categories'
		ordering = ('ordering',)

	def __str__(self):
		return self.title


class Org(models.Model):
	category = models.ForeignKey(Category, related_name='orgs', on_delete=models.CASCADE)
	
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	description = models.TextField(blank = True, null = True)

	website = models.CharField(blank = True, null = True, max_length=255)
	team_size = models.IntegerField(blank = True, null = True)
	country_hq = CountryField(blank_label = '(select headquarters)')
	locations = CountryField(blank_label = '(select office locations)', multiple=True)
	
	is_featured = models.BooleanField(default=False)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-team_size',)


	def __str__(self):
		return self.title

