from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Officer


class OfficerResource(resources.ModelResource):
    class Meta:
        model = Officer
        import_id_fields = ['id']
        skip_unchanged = True


@admin.register(Officer)
class OfficerAdmin(ImportExportModelAdmin):
    resource_class = OfficerResource
    list_display = ('name', 'mobile_number', 'designation', 'city', 'state')
    search_fields = ('name', 'mobile_number', 'designation', 'city', 'state', 'address')
    list_filter = ('state', 'city', 'designation')