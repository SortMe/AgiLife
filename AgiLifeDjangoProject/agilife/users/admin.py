from django.contrib import admin
from .models import UserEvent
from .models import GroupEvent
# Register your models here.
admin.site.register(UserEvent)
admin.site.register(GroupEvent)
