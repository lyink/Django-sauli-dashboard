# your_app/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class RoleBasedRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.user.user_type == 1:  # Admin
                return redirect(reverse('admin_dashboard'))
            elif request.user.user_type == 2:  # Manager
                return redirect(reverse('manager_dashboard'))
            elif request.user.user_type == 3:  # Accountant
                return redirect(reverse('accountant_dashboard'))
        response = self.get_response(request)
        return response
