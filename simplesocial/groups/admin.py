from django.contrib import admin
from . import models
# Register your models here.


#pour l'édition dans la console d'administration
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
