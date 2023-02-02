from core.models import Usuario, Grupos, Tarefas, Topic, conjTopic
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

admin.site.register(Grupos)
admin.site.register(Usuario)
admin.site.register(Tarefas)
admin.site.register(Topic)
admin.site.register(conjTopic)


class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password",'password_confirmation')}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "foto")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
