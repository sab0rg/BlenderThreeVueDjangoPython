from django.shortcuts import render
from apps.orgs.models import Org, Org_BrainRegion, BrainRegion


def dashboard(request):
	orgs = Org.objects.all()
	
	#Gets only the orgs which have the value is_featured set to true
	#orgs = Org.objects.filter(is_featured=True)

	context = {
		'orgs': orgs
		}
		
	return render(request, 'dashboard.html', context)

def contact(request):
	return render(request, 'contact.html')

def about(request):
	return render(request, 'about.html')

def frontpage(request):

	#passing orgs from SQL with Django(python) into the html template
	orgs = Org.objects.all()
	#passing brain regions from SQL with Django(python) into the html template
	brainRegions = BrainRegion.objects.all()
	#passing a mapping between which orgs work on which brain region
	orgBrainRegions = Org_BrainRegion.objects.all()

	context = {
		'orgs': orgs,
		'brainRegions' : brainRegions,
		'orgBrainRegions' : orgBrainRegions,
		}

	return render(request, 'frontpage.html', context)

def threeRefactored1(request):
	orgs = Org.objects.all()

	context = {
		'orgs': orgs
		}

	return render(request, 'threeRefactored1.html', context)