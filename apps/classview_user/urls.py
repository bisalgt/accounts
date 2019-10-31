from django.urls import path
from django.contrib.auth.views import TemplateView

from apps.classview_user import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(template_name='classview_user/login.html'), name='classview_login'),
    path('logout/', views.CustomLogoutView.as_view(), name='classview_logout'),
    path('success/', TemplateView.as_view(template_name='classview_user/success.html'), name='classview_success'),
    path('register/', views.UserCreateView.as_view(), name='classview_register'),
]
