from django.contrib import admin

from .models import Category, Org, BrainRegion, HigherOrderBrainFunctions, BrainRegion_HigherOrderBrainFunctions, Org_BrainRegion

admin.site.register(Category)
admin.site.register(Org)
admin.site.register(BrainRegion)
admin.site.register(HigherOrderBrainFunctions)
admin.site.register(BrainRegion_HigherOrderBrainFunctions)
admin.site.register(Org_BrainRegion)

