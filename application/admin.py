from django.contrib import admin
from .models import Contact, AllProjects

# Register your models here.
#@admin.register(Contact)
admin.site.register(Contact)

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'subject', 'message']



class AllProjectsAdmin(admin.ModelAdmin):
    list_display = ('id','projectCode', 'title', 'description','github_link')  # Specify the fields to display in the admin list view

# Register the AllProjects model with the custom admin class
admin.site.register(AllProjects, AllProjectsAdmin)


# using annotations to register and use database