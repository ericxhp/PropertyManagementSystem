from django.contrib import admin

# Register your models here.
from .models import Asset

# Register your models here.
#Control admin style
class AssetAdmin(admin.ModelAdmin):
    
    list_display = ('asset_num', 'desciption', 'serial_num', 'asset_type',
                    'location','status','owner','assignee','order_num','note')
    list_filter = ('asset_type','status', 'owner', 'assignee')
    search_fields = ('asset_type','status', 'owner', 'assignee')


# Register your models here.
admin.site.register(Asset,AssetAdmin)