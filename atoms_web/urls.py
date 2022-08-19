from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('productos/', include('productos.urls')),
    path('admin/', admin.site.urls),
]