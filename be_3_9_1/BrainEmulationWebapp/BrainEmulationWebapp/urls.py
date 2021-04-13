"""BrainEmulationWebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.core.views import frontpage, contact, about, three, threeRefactored1
from apps.orgs.views import org_profile, category_detail
from apps.favorites.views import favorites

from apps.orgs.api import api_add_to_favorites

urlpatterns = [
	path('admin/', admin.site.urls),

	# API
	path('api/add_to_favorites/', api_add_to_favorites, name='api_add_to_favorites'),

	path('', frontpage, name='frontpage'),
	path('contact/', contact, name='contact'),
	path('about/', about, name='about'),
	path('favorites/', favorites, name='favorites'),

	path('three/', three, name='three'),
	path('three/1', threeRefactored1, name='threeRefactored1'),


	# Org stuff
	path('<slug:category_slug>/<slug:slug>/', org_profile, name='org_profile'),
	path('<slug:slug>/', category_detail, name='category_detail'),

	

    
]
