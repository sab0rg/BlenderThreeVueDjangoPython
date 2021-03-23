from django.shortcuts import render
from apps.orgs.models import Org


def frontpage(request):
	orgs = Org.objects.all()
	
	#Gets only the orgs which have the value is_featured set to true
	#orgs = Org.objects.filter(is_featured=True)

	context = {
		'orgs': orgs
		}
		
	return render(request, 'frontpage.html', context)

def contact(request):
	return render(request, 'contact.html')

def about(request):
	return render(request, 'about.html')

def three(request):
	return render(request, 'three.html')