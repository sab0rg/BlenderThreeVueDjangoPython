from django.shortcuts import render, get_object_or_404

from .models import Org, Category

def org_profile(request, category_slug, slug):
	org = get_object_or_404(Org, slug=slug)

	context={
		'org':org
		}

	return render(request, 'org_profile.html', context)

def category_detail(request, slug):
	category = get_object_or_404(Category, slug=slug)
	orgs = category.orgs.all()

	context={
		'category': category,
		'orgs': orgs
		}

	return render(request, 'category_detail.html', context)