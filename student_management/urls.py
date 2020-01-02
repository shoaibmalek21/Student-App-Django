from django.contrib import admin
from django.urls import path, include
from student.views import user_logout,success,ProfileUpdate,MyProfile,signup,login_page,home

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('survey/', include('survey.urls')),
    path('student/', include('student.urls')),
    path('success/', success, name='user_success'),
    path('logout/', user_logout, name='user_logout'),
    path('profile/', MyProfile.as_view(), name='my_profile'),
    path('profile/update', ProfileUpdate.as_view(), name='update_profile'),

    path('register/',signup,name='register'),
    path('login/', login_page,name='login'),

]
