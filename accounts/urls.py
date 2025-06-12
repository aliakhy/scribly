from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


app_name='accounts'
urlpatterns = [
    path('',login_page,name='login_page'),
    path('logout/', log_out, name='logout_page'),
    path('register/', register, name='register_page'),

    path('profile/edit/', edit_profile, name='edit_profile'),

    path('profile/change_password/',Change_password.as_view(template_name='templates/user/profile/change_password.html'), name='change_password'),
    path('profile/<str:username>/', profile, name='profile_page'),





    # ****password reset url*****
    path('password_reset/',User_password_reset.as_view(),name='password_reset'),
    path('password_reset/done',User_password_reset_done.as_view(),name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',User_password_reset_confirm.as_view(),name='password_reset_confirm'),
    path('password_reset/complete/',User_password_reset_complete.as_view() , name='password_reset_complete'),]
