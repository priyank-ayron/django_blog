
from django.urls import path
from . import views

app_name = 'App_Login'


urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-profile/', views.user_change, name='user_change'),
    path('password/', views.password_change, name='password_change'),
    path('add-profile-image/', views.profile_pic_add, name='profile_pic_add'),
    path('change-profile-image/', views.profile_pic_change, name='profile_pic_change')
]
