from django.conf import settings
from django.urls import path
from .views import admin_dashboard, manager_dashboard, accountant_dashboard
from .views import  register_user, user_list, logout_view,user_login
from .views import edit_user, delete_user, activate_user, deactivate_user

from django.conf.urls.static import static

urlpatterns = [
        path('login/', user_login, name='login'),
    path('register/', register_user, name='register_user'),
    path('users/', user_list, name='user_list'),
    path('user/edit/<int:pk>/', edit_user, name='edit_user'),
    path('user/delete/<int:pk>/', delete_user, name='delete_user'),
    path('user/activate/<int:pk>/', activate_user, name='activate_user'),
    path('user/deactivate/<int:pk>/', deactivate_user, name='deactivate_user'),
    path('logout_view/', logout_view, name="logout"),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('manager_dashboard/', manager_dashboard, name='manager_dashboard'),
    path('accountant_dashboard/', accountant_dashboard, name='accountant_dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
