from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.permissions import AllowAny

from core.views import home
from accounts.views import login_view, logout_view

from envios.views import EmpleadoViewSet, EncomiendaViewSet, HistorialEstadoViewSet
from clientes.views import ClienteViewSet
from rutas.views import RutaViewSet
from sucursales.views import SucursalViewSet
from pagos.views import PagoViewSet

router = DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)
router.register(r'encomiendas', EncomiendaViewSet)
router.register(r'historial-estados', HistorialEstadoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'rutas', RutaViewSet)
router.register(r'sucursales', SucursalViewSet)
router.register(r'pagos', PagoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(home), name='home'),
    # URLs de autenticación
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Incluir URLs de apps
    path('accounts/', include('accounts.urls')),
    path('core/', include('core.urls')),
    # API Routes
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(permission_classes=[AllowAny]), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(permission_classes=[AllowAny], url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(permission_classes=[AllowAny], url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
