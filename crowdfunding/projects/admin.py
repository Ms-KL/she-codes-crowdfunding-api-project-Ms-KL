from django.contrib import admin

from .models import Pledge, Project

# # Register your models here.


# -----------------------
# ADMIN BLOCK
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "goal", "is_open", "date_created", "deadline")


admin.site.register(Project, ProjectAdmin)


class PledgeAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "supporter", "amount", "anonymous", "date_pledged")


admin.site.register(Pledge, PledgeAdmin)
