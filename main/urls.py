from django.urls import path
from . import views

urlpatterns = [
	path('restaurant/<int:id>/', views.home, name='main-page'),
    path('menu/<int:id>/', views.menupage, name='menu-page'),
	path('', views.index, name='index-page'),
]
