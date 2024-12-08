from django.urls import path, include
from inventarioAPP.api.views import PacienteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet, basename='paciente')

urlpatterns = [
    path('', include(router.urls)),
]
