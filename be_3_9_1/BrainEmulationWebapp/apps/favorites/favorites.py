from django.conf import settings


class Favorites(object):
	def __init__(self, request):
		self.session=request.session
		favorites = self.session.get(settings.SESSION_COOKIE_AGE)

		if not favorites:
			favorites = self.session[settings.FAVORITES_SESSION_ID] = {}

		self.favorites = favorites
		
	def add(self, org, want_updates = False):
		org_id = str(org.id)
		org_title = org.title

		if org_id not in self.favorites:
			self.favorites[org_id] = {'want_updates':True, 'id':org_id}

		self.save()

		
		#want udpates needs to be figured out better

	def save(self):
		self.session[settings.FAVORITES_SESSION_ID] = self.favorites
		self.session.modified=True
