from django.db import models
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField


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
	BRAIN_AREAS=[
		('frontal', 'Frontal lobe'),
		('occipit', 'Occipital lobe'),
		('cereb', 'Cerebellum'),
		('temp', 'Temporal lobe'),
		('pariet', 'Parietal lobe'),
		('corpus', 'Corpus Callosum'),
		('pitua', 'Pituitary gland'),
		('stem', 'Brainstem'),
		('periph', 'Peripheral nervous system'),
	]

	#BRAIN_FUNCTIONS=[sdjasdkja]

	
	category = models.ForeignKey(Category, related_name='orgs', on_delete=models.CASCADE)
	
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	what_and_how= models.TextField(max_length=140)
	description = models.TextField(blank = True, null = True)

	concerned_with_brain_area = MultiSelectField(
        choices=BRAIN_AREAS,
        max_choices=len(BRAIN_AREAS),
		default="n/a"
    )


	website = models.CharField(blank = True, null = True, max_length=255)
	team_size = models.IntegerField(null = True)
	country_hq = CountryField(blank_label = '(select headquarters)')
	all_locations = CountryField(blank_label = '(select office locations)', multiple=True)
	
	is_featured = models.BooleanField(default=False)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-team_size',)


	def __str__(self):
		return self.title

