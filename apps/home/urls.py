# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('accountant_dashboard/', views.accountant_dashboard, name='accountant_dashboard'),
       path('organizations/', views.organization_list, name='organization_list'),
    path('organizations/<int:pk>/', views.organization_detail, name='organization_detail'),
    path('organizations/new/', views.organization_create, name='organization_create'),
   path('organization/edit/<int:pk>/', views.edit_organization, name='edit_organization'),
    path('organization/delete/<int:pk>/', views.delete_organization, name='delete_organization'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
