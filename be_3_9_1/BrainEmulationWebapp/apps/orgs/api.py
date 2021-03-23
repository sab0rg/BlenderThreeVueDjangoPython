import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from apps.favorites.favorites import Favorites

from .models import Org

def api_add_to_favorites(request):
	
	#loading the request's body into a variable
	data = json.loads(request.body)
	jsonresponse = {'success': True}
	org_id = data['org_id']
	
	#getting the appropriate org from the database based on the request's org_id
	org = get_object_or_404(Org, pk = org_id)

	#calling a method to add org to favorites
	favorites = Favorites(request)
	favorites.add(org=org)


	return JsonResponse(jsonresponse)
