from django.contrib import admin

# Register your models here.
from devicealert.models import Device_sheet, Log_sheet,Device_type,Log_type,Device_Log_Type

admin.site.register(Device_sheet)
admin.site.register(Log_sheet)
admin.site.register(Device_type)
admin.site.register(Log_type)
admin.site.register(Device_Log_Type)