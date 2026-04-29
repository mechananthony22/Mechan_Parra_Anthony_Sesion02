"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.permissions import AllowAny

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
    path('', RedirectView.as_view(url='/api/schema/swagger-ui/', permanent=False), name='home'),
    path('admin/', admin.site.urls),
    
    # API Routes
    path('api/', include(router.urls)),
    
    # Auth Routes (JWT)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Documentation Routes
    path('api/schema/', SpectacularAPIView.as_view(permission_classes=[AllowAny]), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(permission_classes=[AllowAny], url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(permission_classes=[AllowAny], url_name='schema'), name='redoc'),
]
