from django.contrib import admin
from django.urls import path
from core import views

app_name='core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('producto/', views.producto, name='consultar'),
    path('guardar/', views.guardar, name='guardar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    #muestra el producto
    path('detalle/<int:id>', views.detalle, name='detalle'),
    #actualiza el producto
    path('editar/<int:id>', views.editar, name='editar'),
]