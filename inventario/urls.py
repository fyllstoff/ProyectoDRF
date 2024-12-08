from django.contrib import admin
from django.urls import path, include
from inventarioAPP.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventarioAPP.api.urls')),  
    path('', index, name='index'),  
]
