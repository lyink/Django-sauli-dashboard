# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from .forms import LoginForm,EdituserForm,UserForm
from django.contrib.auth import authenticate, login


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomLoginForm
from apps.home.models import Organization  # Import your Organization model

def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect based on user type
                    if user.user_type == 1:
                        return redirect('admin_dashboard')
                    elif user.user_type == 2:
                        return redirect('manager_dashboard')
                    elif user.user_type == 3:
                        return redirect('accountant_dashboard')
                    else:
                        return redirect('home')  # Default redirection if user type is not matched
                else:
                    messages.error(request, 'Your account has been deactivated. Please contact the administrator.')
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = CustomLoginForm()
    
    # Fetch the first organization instance to display the company logo
    organization = Organization.objects.first()
    
    return render(request, 'login.html', {'form': form, 'organization': organization})

@login_required
def activate_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = True
    user.save()
    messages.success(request, 'User activated successfully.')
    return redirect('user_list')  # Adjust this to your desired redirect URL

@login_required
def deactivate_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.is_active = False
    user.save()
    messages.success(request, 'User deactivated successfully.')
    return redirect('user_list')  # Adjust this to your desired redirect URL


# Create your views here.
from django.shortcuts import render
from .models import User

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})





from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages

@login_required
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        form = EdituserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User profile updated successfully.')
            return redirect('user_list')  # Adjust this to your desired redirect URL
    else:
        form = EdituserForm(instance=user)
    
    return render(request, 'edit_user.html', {'form': form, 'user': user})

@login_required
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Check for AJAX request
            user.delete()
            return JsonResponse({'success': True, 'message': 'User deleted successfully.'})
        else:
            user.delete()
            messages.success(request, 'User deleted successfully.')
            return redirect('user_list')
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # For AJAX, return JSON
        return JsonResponse({'success': False, 'message': 'Invalid request.'})

    return render(request, 'confirm_delete.html', {'user': user})




from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import JsonResponse
from .forms import UserForm


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Redirect to the login page or another page
        else:
            messages.error(request, 'Error creating account')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})












from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Adjust this to the name of your login URL or home page URL




from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def manager_dashboard(request):
    return render(request, 'manager_dashboard.html')

@login_required
def accountant_dashboard(request):
    return render(request, 'accountant_dashboard.html')
