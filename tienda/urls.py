from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Rutas automáticas para API REST
router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)
router.register(r'categorias', views.CategoriaViewSet)

urlpatterns = [
    # Rutas Web
    path('', views.producto_list, name='producto_list'),
    path('productos/nuevo/', views.producto_form, name='producto_form'),
    path('productos/editar/<int:pk>/', views.producto_editar, name='producto_editar'),
    path('productos/eliminar/<int:pk>/', views.producto_eliminar, name='producto_eliminar'),

    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/nueva/', views.categoria_form, name='categoria_form'),
    path('categorias/editar/<int:pk>/', views.categoria_editar, name='categoria_editar'),
    path('categorias/eliminar/<int:pk>/', views.categoria_eliminar, name='categoria_eliminar'),

    # Rutas API REST
    path('api/', include(router.urls)),
]
