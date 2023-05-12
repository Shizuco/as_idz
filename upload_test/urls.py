from django.urls import path
from imageshare import views
urlpatterns = [
    path('', views.UploadView.as_view(), name='index'),
    path('view/<pk>/', views.ImageView.as_view(), name='detail'),
    path('about', views.AboutView.as_view(), name='about'),
    path('rules', views.RulesView.as_view(), name='rules'),
]
