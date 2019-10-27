from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from apps.partial_classview_user import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='partial_classview_user/login.html'), name='partial_login'),
    path('logout/', LogoutView.as_view(template_name='partial_classview_user/logout.html'), name='partial_logout'),
    path("success/", TemplateView.as_view(template_name='partial_classview_user/success.html'), name="partial_success"),
    path("register/", views.UserRegisterView.as_view(), name="partial_register"),
]