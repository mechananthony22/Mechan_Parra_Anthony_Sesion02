from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('encomiendas/', views.encomiendas_list, name='encomiendas_list'),
    path('encomiendas/nueva/', views.encomienda_create, name='encomienda_create'),
    path('encomiendas/<uuid:articulo_id>/', views.encomienda_detail, name='encomienda_detail'),
    path('encomiendas/<uuid:articulo_id>/editar/', views.encomienda_edit, name='encomienda_edit'),
    path('encomiendas/<uuid:articulo_id>/eliminar/', views.encomienda_delete, name='encomienda_delete'),
    path('grupos/', views.grupos_list, name='grupos_list'),
    path('grupos/<uuid:grupo_id>/', views.grupo_detail, name='grupo_detail'),
    path('api/lineas-por-grupo/<uuid:grupo_id>/', views.get_lineas_por_grupo, name='get_lineas_por_grupo'),
]
