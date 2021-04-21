from django.db import models
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from taggit.managers import TaggableManager


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
	#brain_region = models.ForeignKey(BrainRegion, related_name='brainRegion', on_delete=models.CASCADE)

	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	what_and_how= models.CharField(max_length=140)
	description = models.TextField(blank = True, null = True)

	#concerned_with_brain_area = MultiSelectField(
    #    choices=BRAIN_REGION,
    #    max_choices=len(BRAIN_REGION),
	#	default="n/a"
    #)
	#based on the django library https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704 it is well maintained and created by django core devs
	tags = TaggableManager();


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



class BrainRegion(models.Model):
	BRAIN_REGION=[
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

	name= models.CharField(max_length=80)
	slug= models.CharField(max_length=20)
	#associated_higher_order_brain_functions= models.ForeignKey(HigherOrderBrainFunctions, related_name='HOBrainFunctions', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class HigherOrderBrainFunctions(models.Model):
	function= models.CharField(max_length=80)
	slug= models.CharField(max_length=80)
	#BRAIN_FUNCTIONS=[sdjasdkja]
	
	def __str__(self):
		return self.function


#interection m2m for Org and Brain Region
class Org_BrainRegion(models.Model):
	#you use primary_key = True if you do not want to use default field "id" given by django to your model
	#auto_increment_id= models.AutoField(primary_key=True)
    
	org_name= models.ForeignKey(Org, on_delete=models.CASCADE)
	brain_region_name= models.ForeignKey(BrainRegion, on_delete=models.CASCADE)
	
	def __str__(self):
		return (self.org_name.title + self.brain_region_name.name)
	class Meta:
		unique_together = ["org_name", "brain_region_name"]

#interection m2m for Brain Region and Higher Order Brain Function
class BrainRegion_HigherOrderBrainFunctions(models.Model):
	
	brain_region_name= models.ForeignKey(BrainRegion, on_delete=models.CASCADE)
	HO_brain_function= models.ForeignKey(HigherOrderBrainFunctions, on_delete=models.CASCADE)
	#BRAIN_FUNCTIONS=[sdjasdkja]
	
	def __str__(self):
		return (self.brain_region_name.name + self.HO_brain_function.function)
	class Meta:
		unique_together = ["brain_region_name", "HO_brain_function"]