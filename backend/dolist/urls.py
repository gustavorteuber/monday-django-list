
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from core.views import (
    TarefasViewSet,
    UsuarioViewSet,
    GruposViewSet,
    MyTokenObtainPairView,
    TopicViewSet,
    conjTopicViewSet,
    CreateGpViewSet,


)



from uploader.router import router as uploader_router



router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'creategp', CreateGpViewSet)
router.register(r'grupos', GruposViewSet)
router.register(r'tarefa', TarefasViewSet)
router.register(r'addtopic', TopicViewSet)
router.register(r'conjtopic', conjTopicViewSet)










urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("media/", include(uploader_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)