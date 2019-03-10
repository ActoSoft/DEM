from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'references-from', views.ReferencesFromViewSet)
router.register(r'references-to', views.ReferencesToViewSet)

urlpatterns = [
    path('', include(router.urls)),
]