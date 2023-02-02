from core.models import Usuario, Grupos, Tarefas
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

admin.site.register(Grupos)
admin.site.register(Usuario)
admin.site.register(Tarefas)