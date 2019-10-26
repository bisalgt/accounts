from django.urls import path
from django.contrib.auth.views import TemplateView

from apps.function_user import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("register/", views.user_register, name="register"),
    path("success/", TemplateView.as_view(template_name='function_user/success.html'), name="success"),
]
