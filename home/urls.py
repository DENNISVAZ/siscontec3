from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='homepage'),
    path('blender/', views.blender, name='blender'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
