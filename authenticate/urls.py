from django.urls import path
from . import views
app_name = "auth_app"

urlpatterns =[
    path("signup", views.SignupCreateView.as_view(), name="signup")
]