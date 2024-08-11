# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import OrganizationForm



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def index(request):
    user = request.user

    # Redirect based on user type
    if user.user_type == 1:
        return redirect('admin_dashboard')
    elif user.user_type == 2:
        return redirect('manager_dashboard')
    elif user.user_type == 3:
        return redirect('accountant_dashboard')
    else:
        return redirect('home')  # Default redirect if user_type is not matched


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required(login_url="/login/")
def manager_dashboard(request):
    return render(request, 'manager_dashboard.html')

@login_required(login_url="/login/")
def accountant_dashboard(request):
    return render(request, 'accountant_dashboard.html')


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))






from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Organization
def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organization_list.html', {'organizations': organizations})

def organization_detail(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    return render(request, 'organization_detail.html', {'organization': organization})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrganizationForm
from .models import Organization

def organization_create(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if an entry already exists
            if Organization.objects.exists():
                # If an entry exists, add an error message and re-render the form
                messages.error(request, 'An organization entry already exists. Only one entry is allowed.')
                return render(request, 'organization_form.html', {'form': form})
            
            # Save the form data if no entry exists
            form.save()
            return redirect('organization_list')
    else:
        form = OrganizationForm()
    
    return render(request, 'organization_form.html', {'form': form})



from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Organization
from .forms import OrganizationForm  # Ensure you create this form

def edit_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = OrganizationForm(instance=organization)
    return render(request, 'edit_organization.html', {'form': form, 'organization': organization})

def delete_organization(request, pk):
    if request.method == 'POST':
        organization = get_object_or_404(Organization, pk=pk)
        organization.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)
