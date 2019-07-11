from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='widget-index'),
    path('about/', views.about, name='widget-about'),
    path('widget/<int:widget_id>/', views.detail, name='widget-detail'),
 
]
