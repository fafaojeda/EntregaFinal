from django.contrib import admin
from chat.models import Message
from .models import *

# Register your models here.
admin.site.register(Message)
admin.site.register(Blog)
admin.site.register(Avatar)