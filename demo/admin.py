from django.contrib import admin

# Register your models here.
from .models import (
    DemoItem,
    Topic,
    Collection
)

admin.site.register(DemoItem)
admin.site.register(Topic)
admin.site.register(Collection)