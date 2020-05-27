from django.urls import path
from form_app import views

app_name = 'form_app'

urlpatterns = [
    path('signup/', views.user_signup_view, name = 'user_signup'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('my_account/', views.account_view, name = 'my_account'),


]
