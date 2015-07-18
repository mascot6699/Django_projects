from django.contrib import admin
from tracking.models import *

admin.site.register(BannedIP)
admin.site.register(UntrackedUserAgent)
admin.site.register(VisitorsUrls)
admin.site.register(Visitor)
