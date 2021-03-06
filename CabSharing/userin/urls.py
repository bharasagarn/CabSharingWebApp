from django.conf.urls import url
from userin import views
from django.urls import path

app_name = 'userin'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('looking_cab/',views.look_cab,name='looking_cab'),
    path('booked_cab/',views.booked_cab,name='booked_cab'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
]