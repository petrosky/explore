from django.urls import path
from .views import WidgetListView
from . import views

urlpatterns = [
    path('', WidgetListView.as_view(), name='widget-index'),
    path('about/', views.about, name='widget-about'),
    path('widget/<int:widget_id>/', views.detail, name='widget-detail'),
 
]
