from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluimos las rutas de la app empleados en la raíz
    path('', include('empleados.urls')),
]
